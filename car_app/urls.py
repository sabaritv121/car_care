from car_app import views
from django.urls import path


urlpatterns = [
    path('',views.home,name='home'),
    # path('Login_view',views.Login_view,name='Login_view'),
    path('user_add',views.user_add,name = 'user_add'),
    path('admn',views.admn,name='admn')

    
]