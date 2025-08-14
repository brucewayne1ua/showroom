from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from user import views as user_views
from cars import views as car_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("cars/", include("cars.urls")),
    path('register/', user_views.register_user, name='register_user'),
    path('users/', include('user.urls')),  # <-- здесь все пути для users
    path('', car_views.car_list, name='car_list'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
