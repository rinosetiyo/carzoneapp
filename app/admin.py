from django.contrib import admin
from app.models import Team, Car, Contact
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html("<img src='{}' width='40' style='border-radius: 50px;' />".format(object.photo.url))
    thumbnail.short_description = 'Photo'

    list_display = ('id','thumbnail','first_name','designation','created_at')
    search_fields = ('first_name','last_name','designation')
    list_filter = ('designation',)

class CarAdmin(admin.ModelAdmin):
    def photo(self, object):
        return format_html("<img src='{}' width='40' />".format(object.car_photo.url))
    photo.short_description = 'Car'

    list_display = ('id','photo','title','condition','price','milage','fuel_type','created_at','is_featured')
    search_fields = ('title','model')
    list_editable = ('is_featured',)
    list_filter = ('condition','price','milage')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','car_title','customer_need','city','state','email','phone')
    search_fields = ('car_title',)

admin.site.register(Team, TeamAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Contact, ContactAdmin)