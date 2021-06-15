from django.db import models
import datetime
from django.utils import timezone


class Species(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    photo = models.CharField(max_length=200, blank=True)

    #แสดงชื่อแคคตัสในระบบหลังบ้าน
    def __str__(self):
        return self.name



class Cacti(models.Model):
    species_id = models.ForeignKey(Species, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pot_type = models.CharField(max_length=50)
    color_type = models.CharField(max_length=50)
    dob = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    size = models.FloatField(default=0, null=False)
    description = models.CharField(default=None, null=True, max_length=500)
    photo = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.name
