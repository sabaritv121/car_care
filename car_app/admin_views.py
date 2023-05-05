
from django.shortcuts import render,redirect
from django.views import View
from car_app.forms import EmployeeRegister
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


#BASE PAGE
class base(View):
    def get(self,request):
     return render(request,'admn/dashboard.html')


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
    form_class = EmployeeRegister
    template_name = 'admn/home.html'
    success_url = reverse_lazy('home')
    logout_url = 'home'
    raise_exception = True

    def form_valid(self, form):
        u = form.save(commit=False)
        u.is_employee = True
        u.save()
        return super().form_valid(form)    