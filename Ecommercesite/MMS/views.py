from django.shortcuts import render
from .models import products
from django.core.paginator import Paginator

# View for rendering the index page with a list of products
def index(request):
    # Retrieve all product objects from the database
    product_objects = products.objects.all()

    # Adding search functionality using a search bar
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(Title__icontains=item_name)

    # Adding paginator to display a limited number of products per page
    paginator = Paginator(product_objects, 3)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    # Render the index.html template with the filtered and paginated product objects
    return render(request, 'shop/index.html', {'product_objects': product_objects})

# View for rendering the detail page of a specific product
def detail(request, id):
    # Retrieve a specific product object from the database based on the provided id
    product_object = products.objects.get(id=id)

    # Render the detail.html template with the specific product object
    return render(request, 'shop/detail.html', {'product_object': product_object})

# View for rendering the checkout page
def checkout(request):
    # Render the checkout.html template
    return render(request, 'shop/checkout.html')
