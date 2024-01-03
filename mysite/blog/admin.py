from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["title"]}),
        (None, {"fields": ["author"]}),
        ("Date information", {"fields": ["published_date"], "classes": ["collapse"]}),

    ]

    #list_display = ["title", "published_date"]

    list_display = ["title", "author", "published_date"]

    list_filter = ["published_date"]

    search_fields = ["title"]

admin.site.register(Post, PostAdmin)