from django.db import models


# Create your models here.

class Department(models.Model):
    # DEPARTMENTS = [
    #     ('Engineering', 'Engineering'),
    #     ('Purchasing', 'Purchasing'),
    #     ('Quality', 'Quality'),
    # ]
    name = models.CharField(
        max_length=20,
        # choices=DEPARTMENTS,
    )

    def __str__(self):
        return f'{self.name}'


class Project(models.Model):
    name = models.CharField(max_length=30)
    dead_line = models.DateField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.name}'


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

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )
    projects = models.ManyToManyField(
        Project
    )

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name} - Dep: {self.department}'
