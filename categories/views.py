from typing import List, Dict
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import Http404, JsonResponse
from categories.models import Category


def index(request):
    categories = Category.objects.all()
    json_categories = []
    for category in categories:
        image = category.image_set.first()
        category = {
            "category": category,
            "image": image,
            'photo_count': len(category.image_set.all())
        }
        json_categories.append(category)
    context = {
        'categories': json_categories
    }
    return render(request, 'categories/index.html', context)


def show(request, category_id):
    try:

        category = Category.objects.get(id=category_id)
    except ObjectDoesNotExist:
        raise Http404
    images = category.image_set.all()
    context = {
        "name": category.name,
        "images": images,
        'photo_count': len(images)
    }
    return render(request, 'categories/show.html', context)


def all_categories(request) -> JsonResponse:
    categories: List[Category] = Category.objects.all()
    json_categories: List[Dict[str, int]] = [{"name": x.name, "id": x.id} for x in categories]
    return JsonResponse({"data": json_categories})
