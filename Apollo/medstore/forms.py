from django import forms
from medstore.models import Medicine


medic_type = (
        ("t","tablet"),
        ("s","syrup"),
    ) 

# class Medform(ModelForm):
#     class Meta:
#         model = Medicine
#         fields = ["medic_name","disease","medic_price","medic_choice"]
