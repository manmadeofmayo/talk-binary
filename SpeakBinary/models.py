from django.db import models
from django import forms

# Create your models here.
class Visit(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    
class theForm(forms.Form):
    theOneField = forms.CharField(max_length=1000, label="", widget=forms.Textarea())

    
