from django import forms
from django.contrib.auth.forms import UserCreationForm
from car_app.models import Login,AppointmentSchedule
import datetime

class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2','name','phone_number')


class EmployeeRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2','name','phone_number','emp_id')



class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class ScheduleAdd(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    start_time = forms.TimeField(widget=TimeInput,)
    end_time = forms.TimeField(widget=TimeInput, )

    class Meta:
        model = AppointmentSchedule
        fields = ('date', 'start_time', 'end_time')

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start_time")
        end = cleaned_data.get("end_time")
        date = cleaned_data.get("date")
        if start > end:
            raise forms.ValidationError("End Time should be greater than start Time.")

        if date < datetime.date.today():
            raise forms.ValidationError("Date can't be in the past")
        return cleaned_data
      


class UpdateForm(forms.ModelForm):
    

    class Meta:
        model = Login
        fields = ('username','name','phone_number')      