from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'locations/index.html')


def show(request,location_id):
    return render(request,'locations/show.html')