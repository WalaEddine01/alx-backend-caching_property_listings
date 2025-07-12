from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Property

@cache_page(60 * 15)
def property_list(request):
    properties = Property.objects.all()
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
