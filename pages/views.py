from django.shortcuts import render, HttpResponse

# Create your views here.
def hello_home_page(request):
    return HttpResponse("Hello, WOrld!")