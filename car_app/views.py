from django.shortcuts import render,redirect
from car_app.models import Login,AppointmentSchedule
from car_app.forms import LoginRegister,ScheduleAdd
from django.views import View
from django.views.generic import ListView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .filters import UserFilter

# Create your views here.
# def home(request):
#     return render(request,'home.html')

class home(View):
    def get(self,request):
        return render(request,'home.html')


class base(View):
  
    redirect_field_name = "redirect_to"
    def get(salf,request):
        return render(request,'admn/base.html')

        
    
def Login_view(request):
    return render(request,'login.html')




@csrf_exempt
def username_exists(request):
    if request.method == 'POST':
        username = request.POST['username']
        print(username)
        print("hi")
        if Login.objects.filter(username=username).exists():
            return JsonResponse({'exists': False})
        else:
            return JsonResponse({'exists': True})




class UserAddView(View):
    template_name = 'login.html'
    form_class = LoginRegister

    def get(self, request):
        form = self.form_class() 
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            u = form.save(commit=False)
            u.is_user = True
            u.save()
            # return JsonResponse("True",safe=False)
            # return redirect('home')
            return JsonResponse({"success": True})
       
        else:
            username = request.POST.get('uname')
            password = request.POST.get('pass')
            user = authenticate(request, username=username, password=password)
                
            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect('employeeadd')
                elif user.is_user:
                    return redirect('Schedules_user')
                elif user.is_employee:
                    return redirect('emp_base')    
        return render(request, self.template_name, {'form': form})


class UserListView(LoginRequiredMixin, ListView):
    login_url = 'home'
    redirect_field_name = 'home'
    raise_exception = True
    model = Login
    context_object_name = 'data'
    template_name = 'admn/userlist.html'
    paginate_by = 4 # Change the number to set the number of items to display per page
    
    def get_queryset(self):
        queryset = Login.objects.filter(is_user=True).order_by('-id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_queryset()
        paginator = Paginator(data, self.paginate_by)
        page = self.request.GET.get('page')
        context['data'] = paginator.get_page(page)
        context['UserFilter'] = UserFilter(self.request.GET, queryset=self.get_queryset())
        return context

# 

#  ## user list   

# 


# class UserListView(LoginRequiredMixin, ListView):
#     login_url = 'home'
#     redirect_field_name = 'home'
#     raise_exception = True
#     model = Login
#     context_object_name = 'data'
#     template_name = 'admn/userlist.html'
#     paginate_by = 4 # Change the number to set the number of items to display per page
    
#     def get_queryset(self):
#         queryset = Login.objects.filter(is_user=True).order_by('-id')
#         return queryset

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         data = self.get_queryset()
#         paginator = Paginator(data, self.paginate_by)
#         page = self.request.GET.get('page')
#         context['data'] = paginator.get_page(page)
#         return context
    

# 

class EmployeeList(LoginRequiredMixin, ListView):
    login_url = 'home'
    redirect_field_name = 'home'
    raise_exception = True
    context_object_name = 'data'
    template_name = 'admn/emplist.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = Login.objects.filter(is_employee=True).order_by('-id')
        return queryset

    def post(self, request):
        queryset = self.get_queryset()
        paginator = Paginator(queryset, self.paginate_by)
        page_number = request.POST.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'admn/emplist.html', {'page_obj': page_obj})
    
        # return render(request,'admn/emplist.html',{'data':data})



#delete
@csrf_exempt
def delete_user_view(request,id):
    wm=Login.objects.get(id=id)
    wm.delete()
    return redirect('userlist')



## schedule_add

# def schedule_add(request):
    
   
#     form = ScheduleAdd()
#     if request.method == 'POST':
#         form = ScheduleAdd(request.POST)
#         if form.is_valid():
#             form.save()
            
       
#             return JsonResponse('True',safe=False)
        
#             # messages.info(request, ' Schedule Added Successfully')
#         #  return redirect('schedule_add')
#     # else:
#     #     form = ScheduleAdd()
#     return render(request, 'admn/schedule_add.html', {'form': form,'read':read})    

# class ScheduleAddView(CreateView):
    
#     template_name = 'admn/schedule_add.html'
#     form_class = ScheduleAdd
#     success_url = reverse_lazy('ScheduleAddView') # replace 'success' with your success URL name or URL path

#     def form_valid(self,form):
#         form.save()
#         return JsonResponse('True',safe=False)





