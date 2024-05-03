# forms.py

from django import forms
from .models import Freelancer, ClientOpportunity

class FreelancerForm(forms.ModelForm):
    class Meta:
        model = Freelancer
        fields = ['name', 'email', 'bio', 'skills']

class ClientOpportunityForm(forms.ModelForm):
    class Meta:
        model = ClientOpportunity
        fields = ['title', 'description', 'posted_by']
