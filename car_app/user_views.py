from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from car_app.models import AppointmentSchedule,Appointment,Login
from django.contrib import messages
from django.views.generic import ListView
from django.http import  JsonResponse

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



def take_appointment(request, id):
    schedule = AppointmentSchedule.objects.get(id=id)
    u = Login.objects.get(user=request.user)
    appointment = Appointment.objects.filter(user=u , schedule=schedule)
    if appointment.exists():
        messages.info(request, 'You Have Already Requested Appointment for this Schedule')
        return redirect("schedule_cus")
    else:
        if request.method == 'POST':
            obj = Appointment()
            obj.user = u
            obj.schedule = schedule
            obj.save()
            messages.info(request, 'Appointment Booked Successfully')
            # return redirect('appointments')
        #     return JsonResponse({'success': True})
        # else:
        #     return JsonResponse({'success': False})
    return render(request, 'user/user_schedule.html', {'schedule': schedule})        





