from django.forms import ModelForm
from apps.helpdesk.models.Config import Config


class ConfigForm(ModelForm):
    
    class Meta:
        model = Config
        fields = ['email', 'hostname', 'password', 'directory']
