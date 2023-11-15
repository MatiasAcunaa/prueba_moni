from apps.loans.models import Loan
from django import forms

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['first_name', 'last_name','dni','email', 'gender', 'amount']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
        }
