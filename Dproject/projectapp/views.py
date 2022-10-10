
from django.shortcuts import render
from . models import place
from . models import team


def demo(request):
    return render(request,'home.html')