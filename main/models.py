from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Districts(models.Model):
    id = models.BigAutoField(primary_key=True)
    district_name = models.CharField(max_length=200, verbose_name="Имя района")
    town = models.IntegerField(verbose_name="id города")

    def __str__(self):
        return f"{self.district_name}"

class Education_1(models.Model):
    Hight = "high"
    Middle = "middle"
    Low = "low"

    ROLE_CHOICES = (
        (Hight, 'Старшая'),
        (Middle, 'Средняя'),
        (Low, 'Младшая')
    )

    id = models.BigAutoField(primary_key=True)
    study_year = models.IntegerField(verbose_name="Учебный год")
    district_id = models.ForeignKey(Districts, on_delete=models.CASCADE)
    school_type = models.CharField(choices=ROLE_CHOICES, verbose_name="Тип школы", max_length=200)
    school_name = models.CharField(max_length=200, verbose_name="Имя школы")
    school_long = models.FloatField(verbose_name="longitude")
    school_lat = models.FloatField(verbose_name="latitude")
    students_num = models.PositiveIntegerField(verbose_name="количество студентов")
    graduates_num = models.PositiveIntegerField(verbose_name="количество выпускников")

    def __str__(self):
        return f"{self.school_name}: {self.school_type}"



