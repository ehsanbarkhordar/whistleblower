import json

import urllib

from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from khayyam import JalaliDatetime
from persiantools import digits
from rest_framework import permissions, mixins
from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet

from reports.forms import ReportForm, StatusForm
from reports.models import Report
from reports.serializers import GroupSerializer, UserSerializer, ReportSerializer
from reports.utils import unique_reference_number, utc_to_local
from whistleblowers import settings


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


def thanks(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        a = Report.objects.first()
        mm = utc_to_local(a.modified_datetime)
        currenct = JalaliDatetime(mm)
        return render(request, 'thanks.html', {'created_datetime': currenct.strftime("%C"), 'ref_number': "۱۲۳۴۵۶۷۸۹۲"})

    # if a GET (or any other method) we'll create a blank form


def home(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        return render(request, 'home.html', )

    # if a GET (or any other method) we'll create a blank form


def status(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        form = StatusForm()
        # create a form instance and populate it with data from the request:
        return render(request, 'status.html', {"form": form})
    else:
        form = StatusForm(request.POST)
        if form.is_valid():
            report = Report.objects.filter(reference_number=form.cleaned_data["reference_number"]).first()
            if report:
                reference_number = digits.en_to_fa(report.reference_number)
                title = digits.en_to_fa(report.title)
                report_status = digits.en_to_fa(report.get_status_display())
                return render(request, 'status.html', {"reference_number": reference_number,
                                                       "title": title,
                                                       "status": report_status})
            messages.error(request, 'کدپیگیری وارد شده پیدا نشد. لطفا بیشتر دقت کنید!')
    return render(request, 'status.html', {"form": form})

    # if a GET (or any other method) we'll create a blank form


def new_report(request):
    data_site_key = settings.GOOGLE_RECAPTCHA_DATA_SITE_KEY
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if result['success']:
                reference_number = unique_reference_number()
                n_report = form.save(commit=False)
                n_report.reference_number = reference_number
                n_report.save()
                ref_number = digits.en_to_fa(str(reference_number))
                created_datetime = utc_to_local(n_report.created_datetime)
                created_datetime = JalaliDatetime(created_datetime)
                return render(request, 'thanks.html',
                              {'ref_number': ref_number,
                               'created_datetime': created_datetime.strftime('%C')})
            else:
                messages.error(request, 'reCAPTCHA نامعتبر است. لطفا دوباره تلاش کنید.')
    else:
        form = ReportForm()
    return render(request, 'new_report.html', {'form': form, "data_site_key": data_site_key})


# class ReportViewSet(viewsets.ModelViewSet):
#     """
#     A viewset for viewing and editing user instances.
#     """
#     serializer_class = ReportSerializer
#     queryset = Report.objects.all()
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'reports.html'
#
#     def form(self, request, *args, **kwargs):
#         serializer = self.get_serializer()
#         renderer = HTMLFormRenderer()
#         form_html = renderer.render(serializer.data, renderer_context={
#             'template': 'rest_framework/api_form.html',
#             'request': request
#         })
#         return HttpResponse(form_html)
#
#     def get(self, request):
#         content = {'serializer': ReportSerializer}
#         return Response(content)

class ReportViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,

                    GenericViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """
    model = Report
    serializer_class = ReportSerializer
    queryset = Report.objects.all()

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
