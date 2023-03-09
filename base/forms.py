from django import forms
from .models import Contact,Customer,Deal,Task,Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name','email', 'phone', 'website']



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['company','first_name', 'last_name', 'email', 'phone']

class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['title','company', 'amount', 'status']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','deal', 'contact','status','due_date','completed']

