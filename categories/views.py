from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import Http404

# Create your views here.
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
        # import pdb;pdb.set_trace()
        json_categories.append(category)
    context = {
        'categories': json_categories
    }
    # import pdb;pdb.set_trace()

    return render(request, 'categories/index.html', context)


def show(request, category_id):
    try:

        category = Category.objects.get(id=category_id)
    except ObjectDoesNotExist:
        raise Http404
    images = category.image_set.all()
    for image in images:
        print(image)
    # import pdb;
    # pdb.set_trace()
    return render(request, 'categories/show.html')
