from django.contrib import admin
from .models import Data,Department,Designation,Attendence
# Register your models here.

admin.site.register(Data)
admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(Attendence)