from django import forms
from app.models import portfolio

class PortfolioFormulario(forms.ModelForm):
    class Meta:
        model = portfolio
        fields = ['nombre', 'descripcion']
