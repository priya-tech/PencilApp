from .models import AddNotesModel
from django.forms import ModelForm

class AddNotesForm(ModelForm):
    class Meta:
        model=AddNotesModel
        fields=['text']
