from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("detail/<int:pk>", views.detail, name="detail"),
    path("detail/<int:pk>/update/", views.update, name="update"),
    path('detail/<int:pk>/delete/', views.delete, name='delete'),
]
