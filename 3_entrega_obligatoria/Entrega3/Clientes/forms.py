from django.forms import ModelForm
from .models import Clientes

class ClientesFormulario(ModelForm):
    class Meta: 
        model = Clientes
        fields = '_all_'
        #aca en fields all te lo hace automatico 
        #fields=['nombre','apellido','numerodetel','email']

     

