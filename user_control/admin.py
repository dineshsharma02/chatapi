from django.contrib import admin
from . models import CustomUser, Jwt
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Jwt)