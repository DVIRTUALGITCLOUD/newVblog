from django.conf import settings
from django.conf.urls.static import static




from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('blog.urls')),
                  path('users/', include('users.urls')),
                #   path('accounts/', include('django.contrib.auth.urls')),

                  # Used during the development, not recommended in production
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)