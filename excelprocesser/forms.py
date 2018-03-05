from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField(
            widget=forms.FileInput(
                    attrs={
                        "type" :"file",
                        "class":"form-control-file ml-5",
                    }))
