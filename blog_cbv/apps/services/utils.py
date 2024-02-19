"""
В этом файле находятся различные полезные функции для проекта,
поэтому мы ее отделили от других приложений.
"""

from uuid import uuid4
from pytils.translit import slugify


def unique_slugify(instance, slug):
    """
    Генератор уникальных SLUG для моделей, в случае существования такого SLUG.
    """
    model = instance.__class__
    unique_slug = slugify(slug)
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{unique_slug}-{uuid4().hex[:8]}'
    return unique_slug
