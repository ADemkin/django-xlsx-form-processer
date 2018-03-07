from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.encoding import iri_to_uri
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm
from .utils import (load_data_from_xlsx_file,
                    save_data_to_xlsx,
                    get_form_data_from_request)
import os


def index(request):
    return redirect("/upload")


def upload(request):
    if request.POST:
        
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            name, extension = os.path.splitext(file.name)
            
            fs = FileSystemStorage()
            filepath = fs.save(file.name, file)
            
            if extension in ['.xlsx', '.xls'] and file.size > 0:
                request.session['filepath'] = filepath
                request.session['filename'] = file.name
                return editor(request)
            
            else:
                return HttpResponse("Incorrect file type!<br>Please load MS Excel file.")
    
    else:
        form = UploadFileForm()
    
    return render(request, 'excelprocesser/upload.html', {'form':form})


def editor(request):
    context = {}
    
    if request.method == 'POST' and "update" in request.POST:
        xls_data = get_form_data_from_request(request)
        context['items'] = xls_data
        context['message'] = "Поля обновлены."
    
    elif request.method == 'POST' and 'download' in request.POST:
        xls_data = get_form_data_from_request(request)
        request.session['xls_data'] = xls_data
        return download(request)
    
    else:
        fs = FileSystemStorage()
        file = fs.open(request.session['filepath'], mode='rb')
        
        if file:
            context['items'] = load_data_from_xlsx_file(file)
        else:
            context['error'] = 'No xls_file uploaded. Upload xls_file first.'
    
    return render(request, 'excelprocesser/editor.html', context)


def download(request):
    fs = FileSystemStorage()
    file = fs.open(request.session['filepath'], mode='rb')
    fs.delete(request.session['filepath'])
    
    filename = request.session['filename']
    xls_data = request.session['xls_data']
    
    xls_file = save_data_to_xlsx(xls_data, file)
    
    # encode filename to handle non-ASCII symbols
    encoded_filename = iri_to_uri(f"{filename}")
    
    response = HttpResponse(xls_file, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f"attachment; filename*=UTF-8''{encoded_filename}"
    return response
    
