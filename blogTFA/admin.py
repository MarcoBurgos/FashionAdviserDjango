from django.contrib import admin
from .models import Post


def make_published(modeladmin, request, queryset):
    queryset.update(status='DRAFT')
make_published.short_description = "Publicar la nota"

class PostAdmin(admin.ModelAdmin):
    exclude = ('slug', )
    list_display = ('id', 'title', 'subtitle', 'author', 'section_name', 'status')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_per_page = 25
    list_editable =('status',)
    actions = [make_published]

admin.site.register(Post, PostAdmin)
