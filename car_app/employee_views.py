from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView
from car_app.forms import EmployeeRegister
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from car_app.models import AppointmentSchedule,Appointment,Login
from django.http import  JsonResponse
from django.views.decorators.csrf import csrf_exempt


class Emp_base(LoginRequiredMixin,View):
    login_url = 'home'
    redirect_field_name = 'home'
    raise_exception = True
    def get(self,request):
        return render(request,'employee/base.html')


class Schedules(LoginRequiredMixin,ListView):
    login_url = 'home'
    redirect_field_name = 'home'
    raise_exception = True
    def get(self,request):
        data = Appointment.objects.all()
       
        return render(request,'employee/emp_schedule.html',{'data':data})





def approve_appointment(request, id):

    appointment = Appointment.objects.get(id=id)
    print(appointment)
    print("ok")
    appointment.status = 1
    appointment.save()
    return JsonResponse({'status': 'success'})


class AcceptedSchedules(LoginRequiredMixin,ListView):
    login_url = 'home'
    redirect_field_name = 'home'
    raise_exception = True
    def get(self,request):
        data = Appointment.objects.filter(status=1)
       
        return render(request,'employee/emp_accepted.html',{'data':data})



