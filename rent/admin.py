
# Register your models here.
from django.contrib import admin
from .models import Place, RentInfo

class PlaceAdmin(admin.ModelAdmin):
    search_fields = ['pname','location']
admin.site.register(Place,PlaceAdmin)

class RentInfoAdmin(admin.ModelAdmin):
    search_fields = ['pname','pcode']
admin.site.register(RentInfo,RentInfoAdmin)

