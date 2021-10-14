from django.shortcuts import render
from . import models
# Create your views here.


def all_medicines(request):
    medicines = models.Medicine.objects.all()
    return render(request, "medicines/all_medicines.html",
                  {'medicines': medicines})