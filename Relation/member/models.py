from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length =100,help_text = "First Name")
    lastname = models.CharField(max_length = 100,help_text="Last Name")


    def __str__(self):
        return f"{self.firstname}:{self.lastname}"