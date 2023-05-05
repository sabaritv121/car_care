from car_app import views,admin_views,employee_views
from django.urls import path


urlpatterns = [
    # path('',views.home,name='home'),
    path("",views.home.as_view(),name='home'),
    # path('user_add',views.user_add,name='user_add'),
   


    #admin views
    path('admn',admin_views.base.as_view(),name='admn'),
    path('base',views.base.as_view(), name='base'),
    # path('admin_home',admin_views.dashboard.as_view())
    # path('employee_add',admin_views.employee_add,name='employee_add'),
    path('employeeadd', admin_views.EmployeeAddView.as_view(), name='employeeadd'),
    path('userlist', views.UserListView.as_view(), name='userlist'),
    path('EmployeeList',views.EmployeeList.as_view(),name='EmployeeList'),
    path('delete-wm/<int:id>/', views.delete_user_view, name='delete-wm'),

    path('username_exists', views.username_exists, name='username_exists'),
    # path('schedule_add',views.schedule_add,name = 'schedule_add'),
    path('read',views.read,name='read'),
    path("ScheduleAddView",views.ScheduleAddView.as_view(),name='ScheduleAddView'),



    # employee
    path("emp_base",employee_views.Emp_base.as_view(),name='emp_base'),
    path('Schedules',employee_views.Schedules.as_view(),name='Schedules'),



    #user
     path('UserAddView',views.UserAddView.as_view(), name='UserAddView'),
     






    
]