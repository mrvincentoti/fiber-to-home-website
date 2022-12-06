from django.contrib import admin
from .models import *
from django.shortcuts import render

# Register your models here.
admin.site.register(Home)


class HomeAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = Home.objects.all().count()
        print(count)
        if count == 0:
            return True
        return False
