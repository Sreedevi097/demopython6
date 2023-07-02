from django import forms
from . models import task
from . models import task1
class TaskForm(forms.ModelForm):
    class Meta:
        model=task
        fields=['username','password']

class TaskForm1(forms.ModelForm):
    class Meta:
        model=task1
        fields=['name','dob']
