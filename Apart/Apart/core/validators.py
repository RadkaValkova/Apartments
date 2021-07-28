from django.core.exceptions import ValidationError


def positive_value_validator(value):
    if value < 0:
        raise ValidationError('Моля, попълнете стойност по-голяма от нула')
    return value


def max_length_validator(value, ml):
    if len(value) > ml:
        raise ValidationError(f'Уверете се, че символите не са повече от {ml}. В момента са {len(value)}')
    return value


def first_upper_letter_validator(value):
    if value[0].islower():
        raise ValidationError('Изпишете името с главна буква')
    return value


def is_all_digits_validator(value):
    if not value.isdigit():
        raise ValidationError('Полето може да съдържа само цифри')
    return value
