from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from ..properties.utils import get_all_properties

@cache_page(60 * 15)
def property_list(request):
    properties = get_all_properties()
    data = [
        {
            "id": prop.id,
            "title": prop.title,
            "description": prop.description,
            "price": str(prop.price),
            "location": prop.location,
            "created_at": prop.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }
        for prop in properties
    ]
    return JsonResponse({"properties": data})
