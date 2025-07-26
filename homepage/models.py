from django.db import models

class Department (models.Model):
    dep_name  = models.CharField(max_length=50)

    def __str__(self):
        return self.dep_name
    
class Designation (models.Model):
    des_name  = models.CharField(max_length=50)

    def __str__(self):
        return self.des_name

class Data (models.Model):
    
    GENDER_CHOICES = [
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
    ]

    time_created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,null=True,blank=True)
    email = models.EmailField(max_length=50)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    designation = models.ForeignKey(Designation,on_delete=models.SET_NULL,null=True)
    phone_no = models.CharField(max_length=50)
    date_of_birth = models.DateField(max_length=8,null=True,blank=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    pincode = models.CharField(max_length=15)

    def  __str__(self):
        return (f"{self.first_name} {self.last_name}")

class Attendence (models.Model):

    ATTENDENCE_CHOICES = [
        ('Present','Present'),
        ('Absent','Absent'),
        ('Leave','Leave'),
    ]

    employee = models.ForeignKey(Data,on_delete=models.CASCADE)
    date = models.DateField()
    status  = models.CharField(max_length=10,choices=ATTENDENCE_CHOICES)

    def __str__(self):
        return f"{self.employee.first_name} - {self.date} - {self.status}"