from django.contrib import admin
from .models import Restaurant, DeliverooOrders, StuartOrders

# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    search_fields = ['name__icontains']
    
class DeliverooOrdersAdmin(admin.ModelAdmin):
    list_display = ['rest_name', 'start_time', 'finish_time', 'order_number', 'order_fee', 'order_tip', 'order_total']
    ordering = ['rest_name']
    search_fields = ['rest_name__name__icontains']

class StuartOrdersAdmin(admin.ModelAdmin):
    list_display = ['rest_name', 'order_time', 'order_number', 'order_fee', 'order_multiplier', 'order_total']
    ordering = ['rest_name']
    search_fields = ['rest_name__name__icontains']

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(DeliverooOrders, DeliverooOrdersAdmin)
admin.site.register(StuartOrders, StuartOrdersAdmin)