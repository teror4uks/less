from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_url(value):
    url_valudator = URLValidator()
    reg_val = value
    if "http" in reg_val:
        n_value = reg_val
    else:
        n_value = "http://" + reg_val
    try:
        url_valudator(n_value)
    except:
        raise ValidationError("Invalid URL")

    return n_value