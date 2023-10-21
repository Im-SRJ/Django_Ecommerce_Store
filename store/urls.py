from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("product/<slug:slug>/", views.product_detail, name="product_detail"),
    path("categoery/<slug:slug>/", views.category_list, name="category_list"),
]
