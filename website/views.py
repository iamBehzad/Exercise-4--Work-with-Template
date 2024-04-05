from django.shortcuts import render

def index_view(request):
    return render (request, 'website/index.html')
def features_view(request):
    return render (request, 'website/index.html#features')
def gallery_view(request):
    return render (request, 'website/index.html#gallery')
def pricing_view(request):
    return render (request, 'website/index.html#pricing')
def contact_view(request):
    return render (request, 'website/index.html#contact')
def nothing_to_do_view(request):
    return render (request, 'website/index.html#')
