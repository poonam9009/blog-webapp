from django.contrib import admin

from .models import BlogAppPost,Comments
admin.site.register(BlogAppPost)
admin.site.register(Comments)
