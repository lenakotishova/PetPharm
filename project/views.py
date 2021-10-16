from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from . import models
from . import forms

# Create your views here.

SUBJECT = '{name} Wants to share material "{title}" with you.'
BODY = ("{title} at {uri}. {name} shared material with you. "
        "Please take"  "a look at it. {name} has provided "
        "next comment: {comment} ")


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


def share_medicine(request, medicine_id):
    medicine = get_object_or_404(models.Medicine, id=medicine_id)

    sent = False

    if request.method == "POST":
        form = forms.EmailMedicineForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            uri = request.build_absolute_uri(
                medicine.get_absolute_url(),
            )

            subject = SUBJECT.format(name=cd['name'],
                                     title=medicine.title)
            body = BODY.format(title=medicine.title,
                               uri=uri,
                               name=cd['name'],
                               comment=cd['comment'],
            )
            send_mail(subject, body, 'admin@my.com', [cd['to_email'], ])
            sent = True
    else:
        form = forms.EmailMedicineForm()

    return render(request,
                  'medicines/share.html',
                  {'medicine': medicine, 'form': form, 'sent': sent})
