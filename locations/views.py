from typing import List, Dict

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, JsonResponse
from django.shortcuts import render

# Create your views here.
from categories.models import Category
from locations.models import Location


def index(request):
    locations = Location.objects.all()
    json_locations = []
    for location in locations:
        image = location.image_set.first()
        location = {
            "name": location.name,
            'id': location.id,
            "image_url": image.image.url,
            'photo_count': len(location.image_set.all())
        }
        json_locations.append(location)
    context = {
        'locations': json_locations
    }
    return render(request, 'locations/index.html', context)


def show(request, location_id):
    try:
        location = Location.objects.get(id=location_id)
    except ObjectDoesNotExist:
        raise Http404
    images = location.image_set.all()
    context = {
        "name": location.name,
        "images": images,
        'photo_count': len(images)
    }
    return render(request, 'locations/show.html', context)


def get_all_locations(request) -> JsonResponse:
    locations: List[Location] = Location.objects.all()
    json_locations: List[Dict[str, int]] = [{"name": x.name, "id": x.id} for x in locations]
    return JsonResponse({"data": json_locations})
