from django.core.validators import RegexValidator
from django.db import models

phone_regex = RegexValidator(regex=r'^(\+98|0)?9\d{9}$',
                             message="شماره تلفن شما باید در قالب 0930******* باشد.")

BOOL_CHOICES = ((True, 'بلی'), (False, 'خیر'))


class Whistle(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='نام')
    last_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='نام خانوادگی')
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True,
                                    verbose_name='شماره تماس')
    email = models.EmailField(max_length=100, blank=True, null=True, verbose_name='ایمیل')
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='عنوان')
    description = models.TextField(max_length=255, blank=True, null=True,
                                   verbose_name='شرح فساد')

    file = models.FileField(upload_to='documents/', null=True, blank=True, verbose_name='سند')
    contact_you = models.BooleanField(choices=BOOL_CHOICES, default=False,
                                      verbose_name='آیا مایلید با شما تماس بگیریم'
                                                   ' تا در مورد این موضوع بیشتر صحبت کنیم؟')
    committed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Report"
        verbose_name_plural = "Reports"

    def __str__(self):
        return self.title
