from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from django.shortcuts import render

from reports.forms import  ReportForm, ReportInlineFormset


# def model_form_upload(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = DocumentForm()
#     return render(request, 'core/model_form_upload.html', {
#         'form': form
#     })


def home(request):
    if request.method == 'GET':
        report_form = ReportInlineFormset()
        return render(request, 'home.html', {
            'form': report_form
        })
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'home.html', {
            'uploaded_file_url': uploaded_file_url
        })