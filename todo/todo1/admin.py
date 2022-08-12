from django.contrib import admin

# Register your models here.
from .models import data
# Register your models here.

class data1(admin.ModelAdmin):
    list_display = ('title','description', 'priority' ,'created_at')
admin.site.register(data,data1)