from django import forms
from .models import TaskInput

class TaskInputForm(forms.ModelForm):
    class Meta:
        model = TaskInput
        fields = ['raw_data', 'td']
        widgets = {
            'raw_data': forms.Textarea(attrs={'rows': 10, 'cols': 80}),
        }
