from django.contrib import admin
from .models import MenuItem, SiteSetting


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'popup_id', 'order', 'parent']
    list_editable = ['url', 'popup_id', 'order', 'parent']

admin.site.register(MenuItem, MenuItemAdmin)

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['name', 'favicon', 'favicon_preview', 'logo', 'logo_preview']
    readonly_fields = ('logo_preview', 'favicon_preview', 'uploaded_at')
    fields = ('favicon', 'favicon_preview', 'logo', 'logo_preview', 'uploaded_at')

# @admin.register(Logo)
# class LogoAdmin(admin.ModelAdmin):
#     readonly_fields = ('logo_preview',)  # Поля только для чтения
#     list_display = ('name', 'uploaded_at', 'logo_preview')
#     search_fields = ('name',)
