from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Attendance, Grievance, Permission, MealCount, PermissionRequest
from django.utils import timezone

def home1(request):
    return render(request, 'hostel/home1.html')

def add_student(request):
    if request.method == 'POST':
        roll_number = request.POST['roll_number']
        name = request.POST['name']
        gender = request.POST['gender']
        room_number = request.POST['room_number']
        Student.objects.create(
            roll_number=roll_number,
            name=name,
            gender=gender,
            room_number=room_number
        )
        return redirect('student_list')
    return render(request, 'hostel/add_student.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'hostel/student_list.html', {'students': students})

def submit_grievance(request):
    students = Student.objects.all()  # Fetch all students
    if request.method == 'POST':
        student_id = request.POST['student_id']
        description = request.POST['description']
        Grievance.objects.create(student_id=student_id, description=description)
        return redirect('student_list')
    return render(request, 'hostel/submit_grievance.html', {'students': students})

def meal_count(request):
    students = Student.objects.all()
    if request.method == 'POST':
        date = request.POST['date']
        meal_type = request.POST['meal_type']
        student_id = request.POST['student_id']
        count = request.POST['count']

        MealCount.objects.create(date=date, meal_type=meal_type, student_id=student_id, count=count)
        return redirect('view_meal_counts')  # Redirect to view meal counts page

    return render(request, 'hostel/meal_count.html', {'students': students})

def view_meal_counts(request):
    meal_counts = MealCount.objects.all()
    return render(request, 'hostel/view_meal_counts.html', {'meal_counts': meal_counts})

def mark_attendance(request):
    if request.method == 'POST':
        student_ids = request.POST.getlist('student_ids')
        date = request.POST.get('date')
        time_slot = request.POST.get('time_slot')
        status = request.POST.get('status')

        for student_id in student_ids:
            student = get_object_or_404(Student, id=student_id)
            Attendance.objects.create(student=student, date=date, time_slot=time_slot, status=status)

        return redirect('view_attendance')

    students = Student.objects.all()
    return render(request, 'hostel/mark_attendance.html', {'students': students})

def view_attendance(request):
    attendance_records = Attendance.objects.all().order_by('-date')
    return render(request, 'hostel/view_attendance.html', {'attendance_records': attendance_records})

def request_permission(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')  # Assuming you have a way to get student ID
        reason = request.POST.get('reason')
        student = get_object_or_404(Student, id=student_id)
        PermissionRequest.objects.create(student=student, reason=reason)
        return redirect('view_permission_requests')

    students = Student.objects.all()  # Pass students to the template for the dropdown
    return render(request, 'hostel/request_permission.html', {'students': students})

def grievance_report(request):
    grievances = Grievance.objects.all()
    return render(request, 'hostel/grievance_report.html', {'grievances': grievances})

def view_permission_requests(request):
    permission_requests = PermissionRequest.objects.all()
    return render(request, 'hostel/view_permission_requests.html', {'permission_requests': permission_requests})

def update_permission_request(request, request_id):
    permission_request = get_object_or_404(PermissionRequest, id=request_id)

    if request.method == "POST":
        status = request.POST.get('status')
        if status in ['Approved', 'Denied']:
            permission_request.status = status
            permission_request.save()
            return redirect('view_permission_requests')

    return render(request, 'hostel/update_permission_request.html', {'request': permission_request})

def report_grievance(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')  # Get the student ID from the form
        description = request.POST.get('description')
        student = get_object_or_404(Student, id=student_id)
        Grievance.objects.create(student=student, description=description)
        return redirect('view_grievances')

    students = Student.objects.all()  # Pass students to the template for the dropdown
    return render(request, 'hostel/report_grievance.html', {'students': students})

def view_grievances(request):
    grievances = Grievance.objects.all()
    return render(request, 'hostel/view_grievances.html', {'grievances': grievances})

def update_grievance_status(request, grievance_id):
    grievance = get_object_or_404(Grievance, id=grievance_id)

    if request.method == "POST":
        status = request.POST.get('status')
        if status in ['Resolved', 'Rejected']:
            grievance.status = status
            grievance.save()
            return redirect('view_grievances')

    return render(request, 'hostel/update_grievance_status.html', {'grievance': grievance})