from django.shortcuts import render,redirect
from car_app.models import Login,AppointmentSchedule
from car_app.forms import LoginRegister,ScheduleAdd
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

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
            return JsonResponse("True",safe=False)
            # return redirect('home')
        else:
            username = request.POST.get('uname')
            password = request.POST.get('pass')
            user = authenticate(request, username=username, password=password)
                
            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect('employeeadd')
                elif user.is_user:
                    return redirect('home')
                elif user.is_employee:
                    return redirect('emp_base')    
        return render(request, self.template_name, {'form': form})


#username exist
@csrf_exempt
def username_exists(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        u=Login.objects.filter(username=username).exists()
        print("ys")
        if u == True:
            print("ysss")
            return JsonResponse({'exists': True})
        else:
            print("noo")
            return JsonResponse({'exists': False})
#  ## user list   

class UserListView(View):
    
    def get(self, request):
        data = Login.objects.filter(is_user=True)
        return render(request, 'admn/userlist.html',{'data': data})
        

class EmployeeList(View):
     def post(self,request):
        data = Login.objects.filter(is_employee = True)
    
        return render(request,'admn/emplist.html',{'data':data})



#delete

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

class ScheduleAddView(CreateView):
    
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
  