from django.contrib import admin
from .models import Lections

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Lections, PostAdmin)