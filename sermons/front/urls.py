from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.DashBoard, name="dashboard"),
    path("view_sermon/<int:sermon_id>/", views.view_sermon, name="view_sermon"),
    path("see_request/", views.see_request),
    path("user_info/", views.user_info),
    path("private_place/", views.private_place),
    path("staff_place/", views.staff_place),
]