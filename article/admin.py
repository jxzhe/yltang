from django.contrib import admin
from .models import Article, Comment

class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['article', 'content']
    list_display_links = ['article']
    list_editable = ['content']
    list_filter = ['article', 'content']
    search_fields = ['content']

    class Meta:
        model = Comment

admin.site.register(Article)
admin.site.register(Comment, CommentModelAdmin)