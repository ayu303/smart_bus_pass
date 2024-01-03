from django.contrib import admin
from home.models import College , Manager , Route , Student , Pass, AuthUser

# Register your models here.
admin.site.register(College)
admin.site.register(Manager)
admin.site.register(Route)
admin.site.register(Student)
admin.site.register(Pass)
admin.site.register(AuthUser)