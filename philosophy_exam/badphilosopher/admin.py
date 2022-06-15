from django.contrib import admin
from .models import Lections, Seminars, CommentLection, CommentSeminar


class PostAdmin(admin.ModelAdmin):
    pass

class CommentLectionInline(admin.StackedInline):
    model = CommentLection
    extra = 1


@admin.register(Lections)
class LectionsPostAdmin(admin.ModelAdmin):
    list_display = ["number", "name_question", "visible"]
    ordering = ('number',)
    save_as = True
    save_on_top = True
    inlines = [CommentLectionInline]
    list_editable = ("visible",)
    search_fields = ("name_question", "answer")
    list_display_links = ("number", "name_question", )


@admin.register(CommentLection)
class SeminarsPostAdmin(admin.ModelAdmin):
    list_display = ["name", "text", "post"]
    # ordering = ('number',)
    save_as = True
    save_on_top = True


@admin.register(Seminars)
class SeminarsPostAdmin(admin.ModelAdmin):
    list_display = ["number", "name_question", "visible"]
    ordering = ('number',)
    save_as = True
    save_on_top = True
    list_editable = ("visible",)
    search_fields = ("name_question", "answer")
    list_display_links = ("number", "name_question",)

@admin.register(CommentSeminar)
class SeminarsPostAdmin(admin.ModelAdmin):
    list_display = ["name", "text", "post"]
    # ordering = ('number',)
    save_as = True
    save_on_top = True


