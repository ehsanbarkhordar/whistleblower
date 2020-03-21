import random
from datetime import datetime
from django.utils import timezone

from reports.models import Report
from whistleblowers.settings import REFERENCE_NUMBER_LENGTH

random.seed(datetime.now())


def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)


def random_with_n_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return random.randint(range_start, range_end)


def unique_reference_number():
    reference_number = random_with_n_digits(int(REFERENCE_NUMBER_LENGTH))
    if not Report.objects.filter(reference_number=reference_number).exists():
        return reference_number
    else:
        return unique_reference_number()


# def generate_captcha():
#     from captcha.audio import AudioCaptcha
#     from captcha.image import ImageCaptcha
#
#     # audio = AudioCaptcha(voicedir='/path/to/voices')
#
#     import os
#     dirname = os.path.dirname(__file__)
#     font_a = os.path.join(dirname, '../static/fonts/vazir/Vazir.ttf')
#     font_b = os.path.join(dirname, '../static/fonts/sahel/Sahel.ttf')
#
#     image = ImageCaptcha(fonts=[font_a, font_b])
#
#     # data = audio.generate('1234')
#     # audio.write('1234', 'out.wav')
#
#     data = image.generate('1234')
#     # a=image.write('1234', 'out.png')
#     return data

