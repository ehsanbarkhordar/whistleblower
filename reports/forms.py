from django import forms
from reports.models import Whistle


class ReportForm(forms.ModelForm):
    class Meta:
        model = Whistle
        exclude = ['committed_at']
        # widgets = {
        #     # 'first_name': forms.TextInput(attrs={'placeholder': 'اسم خودت'}),
        #     'description': forms.Textarea(
        #         attrs={'placeholder': 'شرح فساد رو خلاصه و دقیق با زمان و مکانش اینجا بنویس.'}),
        # }
