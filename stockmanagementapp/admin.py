from django.contrib import admin
from stockmanagementapp.models import  *
admin.site.register(smsadmin)
admin.site.register(smscategory)
admin.site.register(smssubcategory)
admin.site.register(smsproduct)
admin.site.register(smscustomer)
admin.site.register(smsfinalpurchase)
admin.site.register(smsaccounts)
admin.site.register(smstemppurchase)
admin.site.register(stock)
admin.site.register(smsfinalsale)
admin.site.register(smstempsale)

# Register your models here.
