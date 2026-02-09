from django.contrib import admin
from .models import Tutorial

# Register your models here.
@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug', 'created_at', 'updated_at')
    search_fields = ('title', 'content_md')
    prepopulated_fields = {'slug': ('title',)}
   