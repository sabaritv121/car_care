from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView
from car_app.forms import EmployeeRegister
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from car_app.models import AppointmentSchedule


class Emp_base(LoginRequiredMixin,View):
    login_url = "home"
    def get(self,request):
        return render(request,'employee/base.html')


class Schedules(ListView):
    def get(self,request):
        data = AppointmentSchedule.objects.all()
        return render(request,'employee/emp_schedule.html',{'data':data})

