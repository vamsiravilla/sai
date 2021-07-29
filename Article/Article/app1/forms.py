from django.forms import ModelForm
from .models import Articlemodel

class Articleform(ModelForm):
    class Meta:
        model=Articlemodel
        fields='__all__'

