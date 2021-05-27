from django.db import models

# Create your models here.

class RegisterVehicle(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    phone = models.CharField(max_length=12)
    trucktype = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    tonnage = models.TextField()

    def __str__(self):
        return self.name

class BookVehicle(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    phone = models.CharField(max_length=12)
    fromlocation = models.CharField(max_length=256)
    tolocation = models.CharField(max_length=256)
    trucktype = models.CharField(max_length=256)
    datetime = models.DateTimeField()

    def __str__(self):
        return self.name

class BulkOrder(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    phone = models.CharField(max_length=12)
    fromlocation = models.CharField(max_length=256)
    tolocation = models.CharField(max_length=256)
    trucktype = models.CharField(max_length=256)
    datetime = models.DateTimeField()
    nooftrucks = models.IntegerField()

    def __str__(self):
        return self.email

class Trip(models.Model):

    name = models.ForeignKey('BookVehicle', on_delete=models.CASCADE)
    truck = models.ForeignKey('RegisterVehicle', on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name or ' '
    



    
