from django.shortcuts import render

# Define a static list of products
PRODUCTS = [
    {'name': 'Product 1', 'description': 'This is product 1', 'price': 9.99},
    {'name': 'Product 2', 'description': 'This is product 2', 'price': 14.99},
    {'name': 'Product 3', 'description': 'This is product 3', 'price': 19.99},
    # Add more products as needed
]


def search_view(request):
    query = request.GET.get('q', '')
    if query:
        results = [product for product in PRODUCTS if query.lower() in product['name'].lower()]
    else:
        results = PRODUCTS

    context = {
        'results': results,
        'query': query,
    }
    return render(request, 'search_results.html', context)

def search_page(request):
    return render(request, 'search_form.html')