import itertools
import os

from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class SocialNetwork(models.Model):
    name = models.CharField('Social Network Name', max_length=50)
    url = models.URLField('Social Network URL')

    def __str__(self):
        return self.name

# Модель для изображения, связанного с постом
class PostImage(models.Model):
    post = models.ForeignKey('Post', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField('Image upload', upload_to='posts/images')

    def image_preview(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="100" height="100" />')
        return ""

    image_preview.short_description = "Preview"

    def __str__(self):
        return f"Image for {self.post.title}"


class Logo(models.Model):
    name = models.CharField('Logo Name', max_length=100)
    image = models.ImageField('Logo Image', upload_to='logos/')

    def logo_preview(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="100" height="100" />')
        return ""

    logo_preview.short_description = "Preview"

    def __str__(self):
        return self.name


# Основная модель поста
class Post(models.Model):
    start_date = models.DateField('Start date', auto_now=False)
    invite_until = models.DateField('Invite until', auto_now=False, default=timezone.now)
    is_featured = models.BooleanField('Featured Post', default=False)
    title = models.CharField('Post name', max_length=100)
    slug = models.SlugField('Slug', unique=True, blank=True, null=True)
    short_content = models.TextField('Short description')
    full_content = RichTextField('Full post content')
    social_networks = models.ManyToManyField(SocialNetwork, blank=True, related_name='posts')
    file = models.FileField('Terms and agreements', upload_to='posts/files', blank=True)
    filename = models.CharField(max_length=255, blank=True)
    logo = models.ForeignKey(Logo, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    image_big = models.ImageField('Image upload - big', upload_to='posts/images', null=True, blank=True)
    date_posted = models.DateTimeField('Post date', auto_now_add=True)
    date_updated = models.DateTimeField('Post date updated', auto_now=True)
    #
    # # Превью для image_logo
    # def logo_preview(self):
    #     if self.logo:
    #         return mark_safe(f'<img src="{self.logo.url}" width="100" height="100" />')
    #     return ""
    #
    # logo_preview.short_description = "Logo Preview"

    # Превью для image_big
    def big_image_preview(self):
        if self.image_big:
            return mark_safe(f'<img src="{self.image_big.url}" width="100" height="100" />')
        return ""

    big_image_preview.short_description = "Big Image Preview"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            for i in itertools.count(1):
                if not Post.objects.filter(slug=slug).exists():
                    break
                slug = f'{base_slug}-{i}'
            self.slug = slug

        if self.file and not self.filename:
            self.filename = self.file.name

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


