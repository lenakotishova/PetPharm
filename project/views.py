from django.shortcuts import render, get_object_or_404
from . import models
# Create your views here.


def all_medicines(request):
    medicines = models.Medicine.objects.all()
    return render(request, "medicines/all_medicines.html",
                  {'medicines': medicines})

def detailed_medicine(request, y, m, d, slug):
    medicine = get_object_or_404(models.Medicine,
                                 publish__year=y,
                                 publish__month=m,
                                 publish__day=d,
                                 slug=slug)
    return render(request, "medicines/detailed_medicine.html",
                  {"medicine": medicine})
