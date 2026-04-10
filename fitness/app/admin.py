from django.contrib import admin
from .models import Contact,SEO

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'whatsapp', 'message', 'image')
    search_fields = ('name', 'email', 'whatsapp')
    list_filter = ('name', 'email')

@admin.register(SEO)
class All_pages_SEO(admin.ModelAdmin):
    list_display=['page_name','title','meta_description','keywords','canonical_url']
