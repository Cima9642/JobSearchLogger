from django import forms
from django.utils.timezone import now
from django.forms import ModelForm
from .models import Job
  
class JobSearchForm(forms.Form):
    
    class Meta:
        model = Job
        fields ="__all__"
        
    company = forms.CharField(label='Company', max_length=100)
    rating = forms.ChoiceField(
        label="Motivation",
        choices=[('1', 'Low'), ('2', 'Medium'), ('3', 'High')], required=False
    )
    
    connection_name = forms.CharField(label='Connection Name', max_length=100, required=False)
    status = forms.ChoiceField(
        label='Interview Status',
        choices=[
            ('pending', 'Pending'),
            ('interviewed', 'Interviewed'),
            ('rejected', 'Rejected'),
            ('offered', 'Offered')
        ], required=False
    )
    date_applied = forms.DateField(
        label="Date Applied",
        initial=now().date(),
        widget=forms.DateInput(attrs={'type': 'date'}), required=False
    )
    comments = forms.CharField(widget=forms.Textarea, required=False)
