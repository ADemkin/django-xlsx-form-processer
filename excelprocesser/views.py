from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.encoding import iri_to_uri
from .forms import UploadFileForm
from .utils import (load_data_from_xlsx_file,
                    save_data_to_xlsx,
                    get_form_data_from_request)
import os

# dirty hack due to lack of ideas
file_global = None

def index(request):
    return redirect("/upload")


def upload(request):
    if request.POST:
        
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            name, extension = os.path.splitext(file.name)
            size = file.size
            
            #
            # probably correct way to manage files
            #
            # fs = FileSystemStorage()
            # filename = fs.save(file.name, file)
            #
            # uploaded_file_url = fs.url(filename)
            #
            
            if extension in ['.xlsx', '.xls'] and size > 0:
                return editor(request, file)
            
            else:
                return HttpResponse("Incorrect file type!<br>Please load MS Excel file.")
    
    else:
        form = UploadFileForm()
    
    return render(request, 'excelprocesser/upload.html', {'form':form})


def editor(request, file=None):
    context = {}
    if request.method == 'POST' and "update" in request.POST:
        
        xls_data = get_form_data_from_request(request)
        context['items'] = xls_data
        context['message'] = "Fields updated."
    
    elif request.method == 'POST' and 'download' in request.POST:
        
        xls_data = get_form_data_from_request(request)
        return download(request, xls_data)
    
    else:
        if file:
            # dirty hack
            global file_global
            file_global = file
            
            context['items'] = load_data_from_xlsx_file(file)
        else:
            context['error'] = 'No xls_file uploaded. Upload xls_file first.'
            
    return render(request, 'excelprocesser/editor.html', context)




def download(request, xls_data):
    # dirty hack due to lack of ideas
    global file_global
    if file_global:
        file = file_global
        
    else:
        return HttpResponse("NO FILE TO EDIT")
    
    # Not working here:
    xls_file = save_data_to_xlsx(xls_data, file)

    # encode filename to handle non-ASCII symbols
    encoded_filename = iri_to_uri(f"{xls_file.name}")
    response = HttpResponse(xls_file, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f"attachment; filename*=UTF-8''{encoded_filename}"
    return response
