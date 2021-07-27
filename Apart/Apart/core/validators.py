from django.core.exceptions import ValidationError


def positive_value_validator(value):
    if value <= 0:
        raise ValidationError('Моля, попълнете стойност по-голяма от нула')
    return value


def max_length_validator(value, ml):
    if len(value) > ml:
        raise ValidationError(f'Уверете се, че символите не са повече от {ml}. В момента са {len(value)}')
