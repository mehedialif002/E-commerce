from django.shortcuts import render

# Create your views here.
def index4(request):
    return render(request,'index-4.html')
def product(request):
    return render(request,'product.html')

