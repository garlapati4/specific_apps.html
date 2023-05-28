from django.shortcuts import render

# Create your views here.
def bunny(request):
    return render(request,'bunny.html')
