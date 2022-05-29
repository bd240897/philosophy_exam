from django.contrib import admin
from .models import Lections, Seminars

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Lections, PostAdmin)
admin.site.register(Seminars, PostAdmin)