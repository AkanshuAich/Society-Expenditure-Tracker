from django.contrib import admin
from .models import Exp, Content
# Register your models here.
class ContentAdmin(admin.ModelAdmin):
    list_display = ('user' ,'name', 'event','Date' ,'Current_Balance', 'Total_Amount' , 'Total_Spent')

admin.site.register(Exp)
admin.site.register(Content , ContentAdmin)

