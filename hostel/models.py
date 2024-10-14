from django.db import models

class Student(models.Model):
    roll_number = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.CharField(max_length=10, choices=[('Morning', 'Morning'), ('Evening', 'Evening')])
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')], default='Absent')

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.time_slot} - {self.status}"

class Grievance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    description = models.TextField()
    date_reported = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')  # 'Pending', 'Resolved', 'Rejected'

    def __str__(self):
        return f"{self.student.name} - {self.description} - {self.status}"

class Permission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    reason = models.TextField()
    date_requested = models.DateField(auto_now_add=True)
    approval_status = models.CharField(max_length=20, default='Pending')

class MealCount(models.Model):
    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=10, default='Breakfast')  # e.g., 'Breakfast', 'Lunch', 'Dinner'
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.date} - {self.student.name} - {self.meal_type} - {self.count}"

class PermissionRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    reason = models.TextField()
    date_requested = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')  # 'Pending', 'Approved', 'Denied'

    def __str__(self):
        return f"{self.student.name} - {self.reason} - {self.status}"