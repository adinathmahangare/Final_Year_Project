from django.contrib import admin
from .models import Report,newuser,Doctorinfo,reportd,student,patientdec
# Register your models here.


admin.site.register(Report)
admin.site.register(newuser)
admin.site.register(Doctorinfo)
admin.site.register(reportd)

admin.site.register(student)
admin.site.register(patientdec)
# class TodoAdmin(admin.ModelAdmin):
#     readonly_fields = ('created',)
#
# admin.site.register(Todo, TodoAdmin)
