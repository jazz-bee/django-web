from django.contrib import admin
from blog.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass
# we could customize what is shown on the admin pages but for now, default configuration is enough.

# django admin console: localhost:8000/admin 
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
