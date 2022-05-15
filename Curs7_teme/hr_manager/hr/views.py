from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Employer

def homepage(request):
    print("request is", request)
    all_employers = Employer.objects.all()
    return render(request, "homepage.html", {
        "framework_name": "Django",
        "employers": all_employers
    })

