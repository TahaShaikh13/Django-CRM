from django.db import models


class Data (models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_no = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    pincode = models.CharField(max_length=15)

    def  __str__(self):
        return (f"{self.first_name} {self.last_name}")
