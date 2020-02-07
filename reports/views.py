from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from reports.forms import ReportForm


def home(request):
    if request.method == 'GET':
        report_form = ReportForm()
        return render(request, 'index.html', {
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
