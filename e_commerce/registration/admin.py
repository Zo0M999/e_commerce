from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile

admin.site.register(Profile)

class ProfileInLine(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    field = ['username', 'first_name', 'last_name', 'email']
    inlines = [ProfileInLine]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)