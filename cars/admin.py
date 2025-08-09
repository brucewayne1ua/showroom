from django.contrib import admin
from .models import Brand, Car, CarPhoto, Order

class CarPhotoInline(admin.TabularInline):
    model = CarPhoto
    extra = 1

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand','model','year','price','status')
    list_filter = ('status','brand','year')
    search_fields = ('brand__name','model')
    inlines = [CarPhotoInline]

admin.site.register(Brand)
admin.site.register(Order)
