from django.shortcuts import get_object_or_404, render

from .models import Category, Product


# Create your views here.
def index(request):
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    return render(request, "store/index.html", {"products": products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, "store/single.html", {"product": product})


def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(
        request,
        "store/categoery.html",
        {"products": products, "category": category},
    )
