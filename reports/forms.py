from django import forms
from django.core.exceptions import ValidationError
from persiantools import digits

from reports.models import Report


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        exclude = ['created_datetime', 'reference_number', 'status']
        labels = {
            "reporter_name": "نام گزارش دهنده (اختیاری)",
            "title": "عنوان فساد",
            "description": "شرح فساد رو خلاصه و دقیق با زمان و مکانش اینجا زیر بنویس👇",
            "document": "اگر مدرک یا فایل مرتبطی داری اینجا آپلود کن",
            "phone_number": "تلفن همراه (اختیاری)",
        }

    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)
        # if you want to do it to all of them
        for field in self.fields.values():
            field.error_messages = {'required': 'پر کردن این فیلد اجباری است!'.format(
                fieldname=field.label)}


def validate_number(value):
    if not value.isdigit():
        raise ValidationError("ورودی باید عدد باشد!")


class StatusForm(forms.Form):
    reference_number = forms.CharField(label='کد پیگیری', max_length=32)

    def clean(self):
        self.cleaned_data["reference_number"] = digits.fa_to_en(self.cleaned_data["reference_number"])
        cd = self.cleaned_data
        validate_number(cd.get('reference_number', None))
