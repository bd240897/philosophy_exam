from django.contrib import admin
from .models import Lections, Seminars

class PostAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Lections, PostAdmin)
# admin.site.register(Seminars, PostAdmin)


@admin.register(Lections)
class LectionsPostAdmin(admin.ModelAdmin):
    list_display = ["number", "name_question", "visible"]
    ordering = ('number',)

@admin.register(Seminars)
class SeminarsPostAdmin(admin.ModelAdmin):
    list_display = ["number", "name_question", "visible"]
    ordering = ('number',)