from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'name': 'NAME',
            'email': 'EMAIL',
            'mobilenumber': 'MOBILE NUMBER'
        }
    def __int__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_lable= "select"
