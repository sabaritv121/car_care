from car_app import views,admin_views,employee_views,user_views
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
    path('category/<int:category_id>/toggle-active/', admin_views.toggle_category_active, name='toggle_category_active'),

    path('username_exists', views.username_exists, name='username_exists'),
    # path('schedule_add',views.schedule_add,name = 'schedule_add'),
    path('read',admin_views.read,name='read'),
    path("ScheduleAddView",admin_views.ScheduleAddView.as_view(),name='ScheduleAddView'),
    path("my_logout_view",admin_views.my_logout_view.as_view(),name='my_logout_view'),

    #update
    


    # employee
    path("emp_base",employee_views.Emp_base.as_view(),name='emp_base'),
    path('Schedules',employee_views.Schedules.as_view(),name='Schedules'),
    path('AcceptedSchedules',employee_views.AcceptedSchedules.as_view(),name='AcceptedSchedules'),
    # path('approve_appointment/<int:id>/',employee_views.approve_appointment, name='approve_appointment'),
    # path('approve_appointment/<int:id>/', employee_views.approve_appointment, name='approve_appointment'),
    path('approve_appointment/<int:id>/', employee_views.approve_appointment, name='approve_appointment'),




    #user
     path('UserAddView',views.UserAddView.as_view(), name='UserAddView'),
     path("user_base",user_views.user_base.as_view(),name='user_base'),
     path("Schedules_user",user_views.Schedules_user.as_view(),name='Schedules_user'),
     path('take_appointment/<int:id>/', user_views.TakeAppointmentView.as_view(), name='take_appointment'),
     path('appointments', user_views.AppointmentListView.as_view(), name='appointments'),
]
     






    
