from django.contrib import admin
from .models import Post, PostImage, SocialNetwork, Logo


# Inline для изображений постов
class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1
    readonly_fields = ('image_preview',)
    fields = ('image', 'image_preview')

# Админка для постов
@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo_preview')
    readonly_fields = ('logo_preview',)

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('big_image_preview', 'date_posted', 'date_updated')
    fields = (
        'start_date',
        'invite_until',
        'is_featured',
        'slug',
        'title',
        'short_content',
        'full_content',
        'file',
        'filename',
        'logo',
        'image_big',
        'big_image_preview',
        'date_updated',
        'social_networks',
    )
    search_fields = ('title',)
    list_display = ('title', 'date_updated')
    filter_horizontal = ('social_networks',)
    inlines = [PostImageInline]

# Регистрация модели Post в админке
admin.site.register(Post, PostAdmin)

# Регистрация модели SocialNetwork в админке
@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')  # Для отображения списка соцсетей в админке

