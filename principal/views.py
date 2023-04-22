from django.shortcuts import render

def ladingPage(request):
    return render(request, 'index.html')