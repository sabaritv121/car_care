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
from django.core.paginator import Paginator


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
    template_name = 'employee/emp_schedule.html'
    context_object_name = 'data'
    paginate_by = 5

    def get_queryset(self):
       
        data = Appointment.objects.order_by('-id')
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_queryset()
        paginator = Paginator(data, self.paginate_by)
        page = self.request.GET.get('page')
        context['data'] = paginator.get_page(page)
        return context    









class approve_appointment(LoginRequiredMixin,ListView):
    login_url = 'home'
    redirect_field_name = 'home'
    raise_exception = True

    def post(self,request,id):
        print("hi")
        appointment = Appointment.objects.get(id=id)

        print(appointment)
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



