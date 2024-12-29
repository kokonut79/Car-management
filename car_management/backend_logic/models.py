from django.db import models


class Car(models.Model):
    class Meta:
        verbose_name = 'Car'

    unique_id =  models.CharField(
        max_length=8,
        primary_key=True,
        editable=False,
        unique=True)
    
    production_year = models.IntegerField()
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)     
    license_plate = models.CharField(max_length=50)
    garages = models.ManyToManyField('Garage', through='CarGarage', related_name='car_garage')


class Garage(models.Model):
    class Meta:
     verbose_name = 'Garage'
    
    unique_id = models.CharField(
        max_length=8,
        primary_key=True,
        editable=False,
        unique=True)
    
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    capacity = models.IntegerField()


class CarGarage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=False, blank=False)
    garage = models.ForeignKey(Garage, on_delete=models.CASCADE, null=False, blank=False )
    date_added = models.DateField(auto_now_add=True)


class Maintenance(models.Model):
    class Meta:
        verbose_name = 'Maintenance'

    SERVICE_TYPES = (
        ('Repair', 'Repair'),
        ('Maintenance', 'Maintenance'),
    )

    car = models.ForeignKey(Car, on_delete=models.CASCADE , null=False, blank=False)
    garage = models.ForeignKey(Garage, on_delete=models.CASCADE, null=False, blank=False)
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPES)
    scheduled_date = models.DateField()

