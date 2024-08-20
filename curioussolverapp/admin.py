from django.contrib import admin
from .models import Register

class RegisterAdmin(admin.ModelAdmin):
    list_display=('name','phone_number','email')
    list_filter=('name','phone_number','email')
    search_fields=('name','phone_number','email')

admin.site.register(Register,RegisterAdmin)
