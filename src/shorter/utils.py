import string
import random

def string_generator(size=7, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance=None, size=7):
    code = string_generator(size=size)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode=code).exists()
    if qs_exists:
        code = create_shortcode(size=size)
    return code