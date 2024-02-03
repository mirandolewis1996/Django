from django.db import models

# Create your models here.
class Disease(models.Model):

    disease_name = models.CharField(max_length = 100,help_text = "Enter the disease")


    def __str__(self):
        return self.disease_name
     

class Medicine(models.Model):
    medic_name = models.CharField(max_length = 100, help_text = "Enter the disease")
    disease = models.ManyToManyField(Disease,help_text="Select the disease")
    medic_price = models.PositiveIntegerField(help_text="medicine price")

    medictype = (
        ("t","tablet"),
        ("s","syrup"),
    )   

    medic_choice = models.CharField(max_length = 1,choices = medictype,blank=True,help_text="Select the medicne type",default="t")

    def __str__(self):
        return f"{self.medic_name} : Rs {self.medic_price}/-" 