from django.core.exceptions import ValidationError
import re


def validate_hex_code(value):
    HEX_CODE_REGEX = "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"

    x = re.fullmatch(HEX_CODE_REGEX, value)

    if not x:
        raise ValidationError(f"'{value}' is not a valid hex code.", code="invalid")
