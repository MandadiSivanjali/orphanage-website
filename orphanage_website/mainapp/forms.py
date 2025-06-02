from django import forms
from .models import GeneralRequirement

class GeneralRequirementForm(forms.ModelForm):
    class Meta:
        model = GeneralRequirement
        fields = ['item', 'quantity', 'note']