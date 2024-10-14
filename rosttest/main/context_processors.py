from .models import SiteSetting

def site_settings(request):
    """Передаёт фавиконку и логотип во все шаблоны."""
    try:
        settings = SiteSetting.objects.first()  # Получаем первую запись
    except SiteSetting.DoesNotExist:
        settings = None
    return {'site_setting': settings}