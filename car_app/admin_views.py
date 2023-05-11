
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.edit import CreateView
from car_app.forms import EmployeeRegister,ScheduleAdd
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt
  
from car_app.models import AppointmentSchedule
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout


#BASE PAGE
class base(View):
    def get(self,request):
     return render(request,'admn/dashboard.html')

#logoutview

class my_logout_view(LogoutView):
    template_name = 'login.html' 
    next_page = reverse_lazy('UserAddView') 

# def my_logout_view(request):
#     logout(request)
#     return redirect('home')
# class dashboard(View):


        
# def employee_add(request):
#         form =EmployeeRegister()
       
#         if request.method =='POST':
#             form = EmployeeRegister(request.POST)
#             if form.is_valid():
#                   u= form.save(commit=False)
                
#                   u.is_employee = True
#                   u.save()
                         
                
#                   return redirect('home')    
#         return render(request,'admn/home.html',{'form':form})
    

class EmployeeAddView(LoginRequiredMixin,FormView):
    login_url = '/home/'
    redirect_field_name = 'home'
    form_class = EmployeeRegister
    template_name = 'admn/home.html'
    success_url = reverse_lazy('home')
 
    raise_exception = True

    def form_valid(self, form):
        u = form.save(commit=False)
        u.is_employee = True
        u.save()
        return super().form_valid(form) 
         
    # def form_valid(self, form):
    #     u = form.save(commit=False)
    #     u.is_employee = True
    #     u.save()
    #     return JsonResponse({"success": True})

    # def form_invalid(self, form):
    #     return JsonResponse({"errors": form.errors})



class ScheduleAddView(LoginRequiredMixin,CreateView):
    login_url = '/home/'
    redirect_field_name = 'home'
    raise_exception = True
    template_name = 'admn/schedule_add.html'
    form_class = ScheduleAdd
    success_url = reverse_lazy('ScheduleAddView') # replace 'success' with your success URL name or URL path

    def form_valid(self,form):
        form.save()
        return JsonResponse('True',safe=False)        


#schedule view
def read(request):
    read = AppointmentSchedule.objects.order_by('-id')
    context = {'read':read}
    return render(request, 'admn/result1.html', context)        



#toggle_active schedules

@csrf_exempt
def toggle_category_active(request, category_id):
    try:
        category = AppointmentSchedule.objects.get(id=category_id)
    except AppointmentSchedule.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Category not found'})
    
    category.is_active = not category.is_active
    category.save()
    
    return JsonResponse({'status': 'success', 'is_active': category.is_active})
