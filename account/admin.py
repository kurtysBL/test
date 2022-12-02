from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'email']
    list_display_links = ['email',]
    
admin.site.register(User, UserAdmin)
