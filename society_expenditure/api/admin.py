from django.contrib import admin
from .models import Exp, Content, UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.
class ContentAdmin(admin.ModelAdmin):
    list_display = ('user' , 'event','Date' ,'Current_Balance', 'Total_Amount' , 'Total_Spent')
class UserAdmin(admin.ModelAdmin):
    list_display = ('user' , 'fats' , 'cult' , 'paracosm' , 'photogeeks' , 'tech' , 'vedant' , 'megaheartz' , 'tars' , 'ecell' , 'sports')
admin.site.register(Exp)
admin.site.register(Content , ContentAdmin)
admin.site.register(UserProfile, UserAdmin)
