from django import forms

class PortfolioFormulario(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.IntegerField()