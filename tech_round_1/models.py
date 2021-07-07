from django.db import models

# Create your models here.

#vehicle choices
manufacturer_choices = (
    ("1", "Mahindra & Mahindra ltd"),
    )
model_choices= (
    ("1", "BOLERO CAMPER GOLD 2WD"),
)
vehicle_choices= (
    ("1", "CAMPER"),
)
rto_choices= (
    ("1", "BARBIL,ODISHA"),
)

#engine choices
year_choices= (
    ("1","2014"),
)

fuel_choices= (
    ("1", "DIESEL"),
)

class Vehicle(models.Model):
    sap_code=models.CharField(blank=True , null=True , max_length=70)
    ledger_name=models.CharField(default="ADV TO OD09C8553" , max_length=70 )
    manufacturer=models.CharField(choices = manufacturer_choices , max_length=70 , default="Mahindra & Mahindra ltd")

    model=models.CharField(choices = model_choices , max_length=70 , default="BOLERO CAMPER GOLD 2WD")
    vehicle_type=models.CharField(choices = vehicle_choices , max_length=70 , default="CAMPER")
    base_km=models.IntegerField()
    rto=models.CharField(choices = rto_choices , max_length=70 , default="BARBIL,ODISHA")


    def __str__(self):
        return self.model


    


class Engine(models.Model):

    model_year=models.CharField(choices=year_choices , max_length=70 , default="2014")
    chassis_no=models.CharField(max_length=70)
    fuel_type=models.CharField(choices = fuel_choices , max_length=70 , default="DIESEL")
    old_vehicle=models.CharField(blank=True , null=True, max_length=70)


    def __str__(self):
        return self.chassis_no
    
