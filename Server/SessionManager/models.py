from django.db import models
from django.db.models import CASCADE, SET_NULL


# Create your models here.
# ---Sessions---
class active_sessions(models.Model):
    computer = models.CharField()
    userBarcode = models.CharField()
    startTime = models.TimeField()
    endTime = models.TimeField()

    def authenticate_barcode(self, barcode):
        pass

class timeout_sessions(models.Model):
    userBarcode = models.CharField()
    startTime = models.TimeField()
    endTime = models.TimeField()

class blocked_sessions(models.Model):
    userBarcode = models.CharField()
    note = models.TextField()

class express_sessions(models.Model):
    staffApproved = models.CharField()
    tempBarcode = models.CharField()
    createdTime = models.TimeField()
    expireTime = models.TimeField()

    def generate_tempBarcode(self):
        pass

class multi_session(models.Model):
    userBarcode = models.CharField()
    startTime = models.TimeField()
    endTime = models.TimeField()

# ---Computers---

class computer_zone(models.Model):
    zoneName = models.CharField()

class computer(models.Model):
    computerName = models.CharField()
    zone = models.ForeignKey(computer_zone, on_delete=SET_NULL)

class locked_computer(models.Model):
    computer = models.ForeignKey(computer, on_delete=CASCADE)
