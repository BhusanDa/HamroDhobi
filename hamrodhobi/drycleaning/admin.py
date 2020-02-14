from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Order,Contact
# Register your models here.
admin.site.register(Contact)
#for setting admin panel header
admin.site.site_header="HAMRODHOBI ADMIN PANEL"
class ManageOrder(admin.ModelAdmin):
        list_filter=('date',)



admin.site.register(Order,ManageOrder)
admin.site.unregister(Group)




