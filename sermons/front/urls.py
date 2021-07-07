from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from django.conf import settings

urlpatterns = [
    path("", views.DashBoard, name="dashboard"),
    path('aboutus',views.aboutUs,name='aboutus'),
    path("view_sermon/<int:sermon_id>/", views.view_sermon, name="view_sermon"),
    path("see_request/", views.see_request),
    path("user_info/", views.user_info),
    path("private_place/", views.private_place),
    path("staff_place/", views.staff_place),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)