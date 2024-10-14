from django.db import models
from django.utils.safestring import mark_safe
from filebrowser.fields import FileBrowseField


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    popup_id = models.CharField(max_length=100, null=True, blank=True)
    order = models.PositiveIntegerField(default=0)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

class SiteSetting(models.Model):
    logo = FileBrowseField("Логотип", max_length=200, directory="images/logo/", blank=True, null=True)
    favicon = FileBrowseField("Фавиконка", max_length=200, directory="images/favicon/", blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name="Название логотипа")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def logo_preview(self):
        if self.logo:
            return mark_safe(f'<img src="{self.logo.url}" width="100" height="100" />')
        return ""

    logo_preview.short_description = "Logo Preview"

    def favicon_preview(self):
        if self.favicon:
            return mark_safe(f'<img src="{self.favicon.url}" width="30" height="30" />')
        return ""

    favicon_preview.short_description = "favicon Preview"

    def __str__(self):
        return "Настройки сайта"

    @property
    def favicon_url(self):
        """Возвращает URL фавиконки или иконку по умолчанию."""
        if self.favicon:
            return self.favicon.url
        return '/static/default-favicon.ico'  # Иконка по умолчанию

    @property
    def logo_url(self):
        """Возвращает URL логотипа или логотип по умолчанию."""
        if self.logo:
            return self.logo.url
        return '/static/default-logo.png'  # Логотип по умолчанию

