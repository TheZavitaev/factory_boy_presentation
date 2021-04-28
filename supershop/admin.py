from django.contrib import admin
from .models import Product, Order, OrderProduct

@admin.register(Product)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    fields = ('name', 'description')  

    list_filter = ('name',)

    search_fields = ('name', 'description')

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_address', 'creation_date')
    fields = ('customer_name', 'customer_address', 'creation_date')  

    list_filter = ('customer_name',)

    search_fields = ('customer_name', 'customer_address')

    inlines = [
        OrderProductInline
    ] 
