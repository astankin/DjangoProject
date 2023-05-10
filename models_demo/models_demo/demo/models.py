from django.db import models


# Create your models here.

class Departments(models.Model):
    DEPARTMENTS = [
        ('Engineering', 'Engineering'),
        ('Purchasing', 'Purchasing'),
        ('Quality', 'Quality'),
    ]
    name = models.CharField(
        max_length=20,
        choices=DEPARTMENTS,
    )

    def __str__(self):
        return f'Dep: {self.name}, id: {self.id}'


class Employee(models.Model):
    first_name = models.CharField(
        max_length=50,
    )
    middle_name = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=50,
    )

    departments = models.ForeignKey(
        Departments,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name} - id: {self.id}'


class Project(models.Model):
    name = models.CharField(max_length=30)
    dead_line = models.DateField(
        null=True,
        blank=True,
    )
    employees = models.ManyToManyField(
        to=Employee
    )
