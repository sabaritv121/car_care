from django.test import TestCase

# Create your tests here.



from django.http import JsonResponse

def take_appointment(request, id):
    schedule = AppointmentSchedule.objects.get(id=id)
    u = Login.objects.get(user=request.user)
    appointment = Appointment.objects.filter(user=u , schedule=schedule)
    if appointment.exists():
        messages.info(request, 'You Have Already Requested Appointment for this Schedule')
        return redirect("schedule_cus")
    else:
        if request.method == 'POST':
            obj = Appointment()
            obj.user = u
            obj.schedule = schedule
            obj.save()
            messages.info(request, 'Appointment Booked Successfully')
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})
    return render(request, 'customer/take_appointment.html', {'schedule': schedule})




<!-- Button to trigger the modal -->
<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#appointmentModal">
  Book Appointment
</button>

<!-- Modal -->
<div class="modal fade" id="appointmentModal" tabindex="-1" role="dialog" aria-labelledby="appointmentModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="appointmentModalLabel">Book Appointment</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <form id="appointmentForm" action="{% url 'take_appointment' schedule.id %}" method="post">
        {% csrf_token %}
        <div class="modal-body">
          <label for="name">Name:</label>
          <input type="text" name="name" id="name" class="form-control">
          <label for="email">Email:</label>
          <input type="email" name="email" id="email" class="form-control">
          <input type="hidden" name="schedule_id" value="{{ schedule.id }}">
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
          <button type="submit" class="btn btn-primary">Book Appointment</button>
        </div>
      </form>
    </div>
  </div>
</div>





$(function() {
    $('#appointmentForm').on('submit', function(event) {
        // Prevent the default form submission behavior
        event.preventDefault();

        // Make the AJAX request
        $.ajax({
            url: $(this).attr('action'),
            type: 'POST',
            data: $(this).serialize(),
            dataType: 'json',
            success: function(data) {
                // Handle the response
                if (data.success) {
                    alert('Appointment
