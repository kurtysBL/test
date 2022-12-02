from django.contrib import admin
from .models import Cathegorie, Article


# Register your models here.

class CathegorieAdmin(admin.ModelAdmin):
    exclude = ['author',]
    
    def save_model(self, request, obj, form, change) -> None:
        if not change:
            obj.author = request.user
        return super().save_model(request, obj, form, change)
    

class ArticleAdmin(admin.ModelAdmin):
    exclude = ['author',]
    list_display = ['titre', 'author', 'created_at', 'updated_at']
    list_display_links = ['titre', 'author',]
    
    def save_model(self, request, obj, form, change) -> None:
        if not change:
            obj.author = request.user
        return super().save_model(request, obj, form, change)
    

admin.site.register(Cathegorie, CathegorieAdmin)
admin.site.register(Article, ArticleAdmin)

