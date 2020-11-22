from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['hash_tag', 'content', 'pin']
    # #hash tag, @pin, content 별로 검색기능 넣기
    search_fields = ['hash_tag', 'content', 'pin']


admin.site.register(Post, PostAdmin)
