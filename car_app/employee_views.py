from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView
from car_app.forms import EmployeeRegister
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from car_app.models import AppointmentSchedule,Appointment,Login
from django.http import  JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator



from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from reportlab.pdfgen import canvas



from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

class Emp_base(LoginRequiredMixin,View):
    login_url = 'home'
    redirect_field_name = 'home'
    raise_exception = True
    def get(self,request):
        return render(request,'employee/base.html')


class Schedules(LoginRequiredMixin,ListView):
    login_url = 'home'
    redirect_field_name = 'home'
    raise_exception = True
    template_name = 'employee/emp_schedule.html'
    context_object_name = 'data'
    paginate_by = 5

    def get_queryset(self):
       
        data = Appointment.objects.order_by('-id')
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_queryset()
        paginator = Paginator(data, self.paginate_by)
        page = self.request.GET.get('page')
        context['data'] = paginator.get_page(page)
        return context    









class approve_appointment(LoginRequiredMixin,ListView):
    login_url = 'home'
    redirect_field_name = 'home'
    raise_exception = True

    def post(self,request,id):
        print("hi")
        appointment = Appointment.objects.get(id=id)

        print(appointment)
        appointment.status = 1
        appointment.save()
        return JsonResponse({'status': 'success'})


class AcceptedSchedules(LoginRequiredMixin,ListView):
        login_url = 'home'
        redirect_field_name = 'home'
        raise_exception = True
        def get(self,request):
            data = Appointment.objects.filter(status=1)
            
            return render(request,'employee/emp_accepted.html',{'data':data})




class PDFView(View):
    def get(self, request):
        # Get data from your model

        data = Appointment.objects.all()

        # Create a response object with PDF mime type
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'

        # Create a PDF object
        doc = SimpleDocTemplate(response, pagesize=letter)

        # Create a table and define its style
        table_data = [['customer', 'date', 'Column 3']]
        for obj in data:
            table_data.append([obj.schedule, obj.user ,obj.status])

        table = Table(table_data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), 'grey'),
            ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), 'lightgrey'),
            ('GRID', (0, 0), (-1, -1), 0.25, 'black')
        ]))

        # Add the table to the PDF document and build it
        elements = [table]
        doc.build(elements)

        return response
