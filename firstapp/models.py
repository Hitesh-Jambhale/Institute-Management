from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=35, unique=True)

    def __str__(self):
        return f'{self.name}'


class Teacher(models.Model):
    emp_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    department = models.ManyToManyField(Department, related_name='department_teach')


class Student(models.Model):
    roll_no = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_stud')
