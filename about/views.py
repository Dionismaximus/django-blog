from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    about = About.objects.all().order_by('-updated_on').first()

    return render(
    request,
    "about/about.html",
    {"about": about},
)
