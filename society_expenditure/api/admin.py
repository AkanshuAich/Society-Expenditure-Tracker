from django.contrib import admin
from .models import Exp, Content
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.
class ContentAdmin(admin.ModelAdmin):
    list_display = ('user' , 'event','Date' ,'Current_Balance', 'Total_Amount' , 'Total_Spent')
admin.site.register(Exp)
admin.site.register(Content , ContentAdmin)
