from django.core.validators import RegexValidator
from django.db import models

phone_regex = RegexValidator(regex=r'^(\+98|0)?9\d{9}$',
                             message="شماره تلفن شما باید در قالب 0930******* باشد.")


class Report(models.Model):
    reference_number = models.CharField(max_length=32, unique=True, db_index=True)
    reporter_name = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    document = models.FileField(upload_to='documents/', null=True, blank=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Report"
        verbose_name_plural = "Reports"

    def __str__(self):
        return self.title
