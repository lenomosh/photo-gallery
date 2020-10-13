from typing import List
from django.http import JsonResponse, Http404

from images.models import Image


def search(request) -> any:
    location_id: int = request.GET.get('location_id', None)
    category_id: int = request.GET.get('category_id', None)
    if location_id and category_id:
        images: List[Image] = Image.objects.filter(category_id=category_id, location_id=location_id).all()
        if len(images) > 0:
            images = [
                {
                    "url": x.image.url,
                    "location": x.location_id.name,
                    "category": x.category_id.name,
                    "name": x.name,
                    "id": x.id
                } for x in images]
            return JsonResponse(dict(data=images))
        else:
            return JsonResponse(dict(data=[]))
    else:
        return Http404('No result Found')
