from django.contrib import admin
from bankapi.models import Bank
# Register your models here.

class BankAdmin(admin.ModelAdmin):
    list_display = ['ifsc','bank_id','bank_name','branch','address','city','district','state']


admin.site.register(Bank,BankAdmin)