from django.db import models

# Create your models here.
class Area(models.Model):
    area_id = models.IntegerField(primary_key=True)
    area_name = models.CharField(max_length=100)

class Department(models.Model):
    department_id = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=255)

    def __str__(self):
        return self.department_namecr