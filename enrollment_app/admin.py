from django.contrib import admin
from enrollment_app.models import User

# Register your models here.
#admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
   list_display = ('id','name','email','passowrd')