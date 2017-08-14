import string
import random

from django.conf import settings

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 7)

def string_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance=None, size=SHORTCODE_MIN):
    code = string_generator(size=size)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode=code).exists()
    if qs_exists:
        code = create_shortcode(size=size)
    return code