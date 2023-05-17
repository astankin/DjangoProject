from django.core.exceptions import ValidationError


def plant_name_validator(value):
    if not value.isalpha():
        raise ValidationError('Plant name should contain only letters!')