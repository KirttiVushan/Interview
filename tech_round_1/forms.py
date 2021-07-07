from django import forms
from .models import Vehicle , Engine

class Vehicle_field(forms.ModelForm):
	class Meta:
		model=Vehicle
		fields='__all__'


class Engine_field(forms.ModelForm):
    class Meta:
        model=Engine
        fields='__all__'