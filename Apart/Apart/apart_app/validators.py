from django.core.exceptions import ValidationError


def positive_value_validator(value):
    if value <= 0:
        raise ValidationError('Моля, попълнете стойност по-голяма от нула')
    return value
