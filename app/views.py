from django.shortcuts import render

# Create your views here.

def cdn_bs(request):
    return render(request,'cdn_bs.html')