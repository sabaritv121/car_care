from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from car_app.models import AppointmentSchedule,Appointment,Login
from django.contrib import messages
from django.views.generic import ListView
from django.http import  JsonResponse
from django.shortcuts import get_object_or_404

class user_base(LoginRequiredMixin,View):
    login_url = 'home'
    redirect_field_name = 'home'
    raise_exception = True
    def get(self,request):
        return render(request,'user/user_base.html')



#user view schedules  

class Schedules_user(LoginRequiredMixin,ListView):
    login_url = 'home'
    redirect_field_name = 'home'
    raise_exception = True
    def get(self,request):
        data = AppointmentSchedule.objects.filter(is_active = True)
        return render(request,'user/user_schedule.html',{'data':data})      





class TakeAppointmentView(LoginRequiredMixin,View):
    login_url = 'home'
    redirect_field_name = 'home'
    raise_exception = True

    def get(self, request, id):
        schedule = AppointmentSchedule.objects.get(id=id)
        u = Login.objects.get(username=request.user)
        appointment = Appointment.objects.filter(user=u, schedule=schedule)
        if appointment.exists():
            messages.info(request, 'You have already requested an appointment for this schedule.')
            return redirect('Schedules_user')
        return render(request, 'user/take_appointment.html', {'schedule': schedule})

    def post(self, request, id):
        schedule = AppointmentSchedule.objects.get(id=id)
        u = Login.objects.get(username=request.user)
        appointment = Appointment.objects.filter(user=u, schedule=schedule)
        if appointment.exists():
            messages.info(request, 'You have already requested an appointment for this schedule.')
            return redirect('Schedules_user')
        else:
            obj = Appointment(user=u, schedule=schedule)
            obj.save()
            messages.success(request, 'Appointment booked successfully.')
            return redirect('appointments')
        
        





class AppointmentListView(LoginRequiredMixin,ListView):
    login_url = 'home'
    redirect_field_name = 'home'
    raise_exception = True
 
    model = Appointment
    context_object_name = 'appointment'
    template_name = 'user/appointments.html'

    def get_queryset(self):
        customer = get_object_or_404(Login, username=self.request.user)
        queryset = super().get_queryset().filter(user=customer).select_related('schedule')
        return queryset
        # print(queryset)