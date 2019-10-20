from django.db import models

# Create your models here.

class AddNotesModel(models.Model):
    text=models.CharField(max_length=200)
    id=models.AutoField(primary_key=True)
