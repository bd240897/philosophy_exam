from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class LectionsPostAdmin(admin.ModelAdmin):
    # list_display = ["number", "name_question", "visible"]
    # ordering = ('number',)
    save_as = True
    save_on_top = True