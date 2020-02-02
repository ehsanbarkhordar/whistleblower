from django.conf import settings
from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True, verbose_name='توضیحات')
    document = models.FileField(upload_to='documents/', verbose_name='سند')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان آپلود سند')

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"

    def __str__(self):
        return self.description


class Report(models.Model):
    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='گزارشگر')
    title = models.CharField(max_length=100, verbose_name='عنوان')
    text = models.TextField(verbose_name='متن گزارش')
    document = models.ForeignKey(Document, on_delete=models.CASCADE, verbose_name='سند')
    committed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Report"
        verbose_name_plural = "Reports"

    def __str__(self):
        return self.title
