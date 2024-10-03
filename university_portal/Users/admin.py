from django.contrib import admin
from .models import Students, Faculty, Admin

# Register your models here.
admin.site.register(Students)
admin.site.register(Faculty)
admin.site.register(Admin)
