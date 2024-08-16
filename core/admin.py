from django.contrib import admin
from .models import Color, Size, Category, SubCategory, Customer, Product, Order, OrderItem, ShippingAddress, InventoryModel, ReviewModel
# Register your models here.

class ColorModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name', 'slug']

class SizeModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name', 'slug']

class CategoryModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name', 'slug']

class SubCategoryModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name', 'slug']


admin.site.register(Color, ColorModelAdmin)
admin.site.register(Size, SizeModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(SubCategory, SubCategoryModelAdmin)
admin.site.register(Customer)
admin.site.register(InventoryModel)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(ReviewModel)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

