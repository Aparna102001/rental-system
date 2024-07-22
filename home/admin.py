from django.contrib import admin
from .models import Vehicle
class TravelAdmin(admin.ModelAdmin):
    list_display=('name','number','driver','type','fare','seats','image')
admin.site.register(Vehicle,TravelAdmin)
from . models import Register,Agency,Agent_Register,bookdetails

admin.site.register(Agency)
admin.site.register(Register)

admin.site.register(Agent_Register)
admin.site.register(bookdetails)
# Register your models here.
