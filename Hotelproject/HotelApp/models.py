from django.contrib.auth.models import User
from django.db import models



class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    employment_year = models.IntegerField()
    employee_type = {
        ("x", "higienicar"),
        ("r", "recepcioner"),
        ("m", "menadzer")
    }
    type = models.CharField(max_length=1, choices=employee_type)

class Room(models.Model):
    number = models.IntegerField()
    bed_number = models.IntegerField()
    has_balcony = models.BooleanField()
    is_clean = models.BooleanField()
    employees = models.ManyToManyField(Employee)
    def __str__(self):
        return f'{self.number}'

class Reservation(models.Model):
    code = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField()
    is_reserved = models.BooleanField(default=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.employee.type}'


class EmployeeRoom(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.employee} - {self.room}'