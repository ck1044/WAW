from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['hash_tag', 'content']
    # #hash tag, @pin, content 별로 검색기능 넣기
    search_fields = ['hash_tag', 'content']


admin.site.register(Post, PostAdmin)
