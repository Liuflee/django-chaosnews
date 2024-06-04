# appchaosnews/templatetags/custom_filters.py
from django import template
from datetime import datetime
from django.utils import timezone
from django.utils.timesince import timesince, timeuntil

register = template.Library()

@register.filter
def human_readable_time(value):
    now = timezone.now()
    if value.tzinfo is None:
        value = timezone.make_aware(value, timezone.get_current_timezone())
    
    delta = now - value
    
    if delta.days >= 365:
        years = delta.days // 365
        return f"hace más de {years} {'año' if years == 1 else 'años'}"
    elif delta.days >= 30:
        months = delta.days // 30
        return f"hace más de {months} {'mes' if months == 1 else 'meses'}"
    elif delta.days >= 7:
        weeks = delta.days // 7
        return f"hace más de {weeks} {'semana' if weeks == 1 else 'semanas'}"
    elif delta.days >= 1:
        return f"hace más de {delta.days} {'día' if delta.days == 1 else 'días'}"
    elif delta.seconds >= 3600:
        hours = delta.seconds // 3600
        return f"hace más de {hours} {'hora' if hours == 1 else 'horas'}"
    elif delta.seconds >= 60:
        minutes = delta.seconds // 60
        return f"hace más de {minutes} {'minuto' if minutes == 1 else 'minutos'}"
    else:
        return "hace unos segundos"