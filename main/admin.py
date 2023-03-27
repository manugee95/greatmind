from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    prepopulated_fields = {'slug':('name',)}

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['id', 'category', 'name', 'price', 'uploaded', 'edited']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'sent']

class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'furniture', 'price', 'amount', 'paid']

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'amount', 'paid', 'purchase_date']

admin.site.register(AppInfo)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Customer)
admin.site.register(Cart, CartAdmin)
admin.site.register(Payment, PaymentAdmin)
