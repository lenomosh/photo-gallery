from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', include('pages.urls')),
                  path('images', include('images.urls')),
                  path('categories/', include('categories.urls')),
                  path('locations/', include('locations.urls')),
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
