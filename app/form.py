from django.forms import ModelForm
from .models import Packages

class PackageForm(ModelForm):
    class Meta:
        model=Packages
        fields='__all__' 
