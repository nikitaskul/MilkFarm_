from django import template
from django.db.models import Count, F

from products.models import Category


register = template.Library()


@register.inclusion_tag('products/category.html')
def show_categories():
    # categories = Category.objects.all()
    categories = Category.objects.annotate(cnt=Count('products', filter=F('products__available'))).filter(cnt__gt=0)
    return {
        'categories': categories
    }
