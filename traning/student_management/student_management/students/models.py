from django.db import models

from django.core.validators import MinLengthValidator

from ..students.validators import profile_name_validator


class Student(models.Model):
    student_number = models.PositiveIntegerField(
        max_length=256
    )
    first_name = models.CharField(
        max_length=50,
        validators=[
            profile_name_validator
        ]
    )
    last_name = models.CharField(
        max_length=50,
        validators=[
            profile_name_validator
        ]
    )
    email = models.EmailField(max_length=100)
    field_of_study = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2)
        ]
    )
    gpa = models.FloatField()

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'
