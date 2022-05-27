from django.contrib import admin
from .models import lections

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(lections, PostAdmin)