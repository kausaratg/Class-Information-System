from django.contrib import admin
from post.models import Post, ClassGroup, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(ClassGroup)
admin.site.register(Comment)
