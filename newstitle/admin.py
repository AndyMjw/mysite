from django.contrib import admin
from .models import Newstitle

@admin.register(Newstitle)
class NewstitleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "author", "is_deleted", "created_time", "last_updated_time")
    ordering = ("-id",)
# Register your models here.
#admin.site.register(Newstitle)