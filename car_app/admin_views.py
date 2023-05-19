
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.edit import CreateView
from car_app.forms import EmployeeRegister,ScheduleAdd,UpdateForm
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt
  
from car_app.models import AppointmentSchedule,Login
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from django.views.generic import ListView
from django.core.paginator import Paginator
from datetime import datetime, timedelta


#BASE PAGE
class base(View):
    def get(self,request):
     return render(request,'admn/dashboard.html')

#logoutview

class my_logout_view(LogoutView):
    template_name = 'login.html' 
    next_page = reverse_lazy('UserAddView') 

# 
    

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


#scheduleadd

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
    data = datetime.now()+ timedelta(days=1)
    # if date < datetime.date.today():
    print(data)
    read = AppointmentSchedule.objects.filter(date = data)
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


#employee list

class EmpList(LoginRequiredMixin, ListView):
    login_url = 'home'
    redirect_field_name = 'home'
    raise_exception = True
    model = Login
    context_object_name = 'data'
    template_name = 'admn/employees.html'
    paginate_by = 4 
    
    def get_queryset(self):
        queryset = Login.objects.filter(is_user=True).order_by('-id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_queryset()
        paginator = Paginator(data, self.paginate_by)
        page = self.request.GET.get('page')
        context['data'] = paginator.get_page(page)
        return context




#search
# class SearchView(View):
#     def get(self, request):
#         query = request.GET.get('q', '')
#         results = Login.objects.filter(name__icontains=query)
#         data = [{'id': result.id, 'name': result.name,'phone_number': result.phone_number} for result in results]
#         return JsonResponse({'results': data})



def edit(request,id):
    obj = Login.objects.get(id=id)
    print(obj)
    print(obj.name)
    print(obj.phone_number)

    form = UpdateForm()

    context = {
        'obj': obj,
        'form': form,
    }
    return render(request,'admn/edit.html',context)


   
def post_detail_data_view(request, pk):
    
        obj = Login.objects.get(pk=pk)
        data = {
            'id': obj.id,
            'username': obj.username,
            'phone_number': obj.phone_number,
            'name': obj.name,
            
            
        }
        return JsonResponse({'data': data})   



def update_post(request, pk):
    obj = Login.objects.get(pk=pk)
   
    if request.method=='POST':
        new_title = request.POST.get('title')
        print(new_title)
        new_name= request.POST.get('name')
        new_phone = request.POST.get('phone')
        obj.username = new_title
        obj.name = new_name
        obj.phone_number = new_phone
        obj.save()
        return JsonResponse({
            'title': new_title,
            'name': new_name,
            'phone':new_phone
        })        