import random
from datetime import datetime

from reports.models import Report
from whistleblowers.settings import REFERENCE_NUMBER_LENGTH

random.seed(datetime.now())


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
