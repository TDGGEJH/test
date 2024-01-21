from django.forms import ModelForm, Textarea, TextInput
from .models import Zapis

class Create(ModelForm):
    class Meta:
        model = Zapis
        fields = ['name','desk']
        widgets = {
            'name':TextInput(attrs={
                'placeholder':'Название'
            }),
            'desk':Textarea(attrs={
                'placeholder':'описание'
            })
        }