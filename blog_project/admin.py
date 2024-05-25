from django.contrib import admin
from .models import *

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title","author","date","get_tags")

class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
