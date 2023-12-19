from django.contrib import admin

# Register your models here.
from .models import Books, Students

admin.site.register(Books)
admin.site.register(Students)
