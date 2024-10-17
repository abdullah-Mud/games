from django.shortcuts import render
from .models import Product ,Photo
from django.shortcuts import render, get_object_or_404
def product_list(request):
    search_query = request.GET.get('search')
    products = Product.objects.all()
    photos = Photo.objects.all()
    if search_query:
        products = products.filter(name__icontains=search_query)
    
    return render(request, 'Game_Store/product_list.html', {'products': products , 'photos': photos})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'Game_Store/product_detail.html', {'product': product})
   

def about(request):
    return render(request, 'Game_Store/about.html')



    
  