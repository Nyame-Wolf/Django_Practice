from django.shortcuts import render


def home(request):
    return render(request,'blog_app/home.html')
def about(request):
    return render(request,'blog_app/about.html')
