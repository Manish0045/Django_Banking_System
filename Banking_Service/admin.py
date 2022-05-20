from django.contrib import admin
from .models import Customers, transactiondetail
# Register your models here.
admin.site.register(Customers)
admin.site.register(transactiondetail)