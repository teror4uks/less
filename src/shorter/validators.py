from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_url(value):
    url_valudator = URLValidator()
    value_1_invalid = False
    value_2_invalid = False

    try:
        url_valudator(value)
    except:
        value_1_invalid = True

    value_2_url = "http://" + value

    try:
        url_valudator(value_2_url)
    except:
        value_2_invalid = True

    if value_1_invalid and value_2_invalid:
        raise ValidationError("Invalid URL")

    return value