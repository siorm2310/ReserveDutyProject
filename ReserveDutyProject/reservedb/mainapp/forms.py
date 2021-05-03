from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    last_here = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}), label='תאריך אחרון')