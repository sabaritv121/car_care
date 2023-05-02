from django.shortcuts import render,redirect
from car_app.forms import LoginRegister,EmployeeRegister
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def Login_view(request):
    return render(request,'login.html')





def user_add(request):
    form1=LoginRegister()
    print("hi")
    if request.method =='POST':
         form1 = LoginRegister(request.POST)
        

         if form1.is_valid():
                print("hi")
                u= form1.save(commit=False)
                print("k")
                u.is_user = True
                u.save()
                print("ok")
                
                return redirect('home')

         else :
                username = request.POST.get('uname')
                password = request.POST.get('pass')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                if user.is_staff:
                    return redirect('admn')   
                if user.is_user:
                    return redirect('home')    
                

    return render(request,'login.html', {'form1': form1})


def admn(request):
    return render (request,'admn/dashboard.html')



# def employee_add(request):
#     form1=EmployeeRegister()
#     if request.method =='POST':
#          form1 = LoginRegister(request.POST)

#          if form1.is_valid():
#                 user = form1.save(commit=False)
#                 user.is_user = True
#                 user.save()
                
#                 return redirect('home')

#     return render(request, 'login.html', {'form1': form1})



