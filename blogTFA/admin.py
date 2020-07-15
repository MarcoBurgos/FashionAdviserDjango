from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


def make_published(modeladmin, request, queryset):
    queryset.update(status='PUBLISHED')
make_published.short_description = "Publicar la(s) nota(s) marcadas"

def make_drafted(modeladmin, request, queryset):
    queryset.update(status='DRAFT')
make_drafted.short_description = "Retirar la(s) nota(s) del sitio"

class PostAdmin(admin.ModelAdmin):
    exclude = ('slug', )
    list_display = ('id', 'title', 'subtitle', 'author', 'category_name', 'status')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_per_page = 25
    list_editable =('status',)
    list_filter = ('status',)
    actions = [make_published, make_drafted]
    # summernote_fields = ('post_content',)


admin.site.register(Post, PostAdmin)
