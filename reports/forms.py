from django import forms
from reports.models import Document, Report
from django.forms.models import inlineformset_factory


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        exclude=[]

#
class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        exclude = ['committed_at', 'account']


ReportInlineFormset = inlineformset_factory(Document, Report, extra=1, form=DocumentForm)
