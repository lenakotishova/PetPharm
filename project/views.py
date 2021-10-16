from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
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


def profile(request):
    return render(request, "profile.html", {'user': request.user})


def register(request):
    if request.method == "POST":
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_user = form.save(commit=False)
            new_user.set_password(cd['password'])
            new_user.save()
            models.Profile.objects.create(user=new_user)

            return render(request, "registration_complete.html",
                          {"user": new_user})

    else:
        form = forms.UserRegistrationForm()
        return render(request, "register.html", {'form': form})


def edit_profile(request):
    if request.method == "POST":
        user_form = forms.UserEditForm(request.POST, instance=request.user)
        profile_form = forms.ProfileEditForm(request.POST,
                                             instance=request.user.profile,
                                             files=request.FILES)
        if all((user_form.is_valid(), profile_form.is_valid())):
            user_form.save()
            if not profile_form.cleaned_data['photo']:
                profile_form.cleaned_data['photo'] = request.user.profile.photo
            profile_form.save()
            return render(request, "profile.html", {'user': request.user})

    else:
        user_form = forms.UserEditForm(instance=request.user)
        profile_form = forms.ProfileEditForm(request.POST, instance=request.user.profile)

    return render(request, "edit_profile.html", {'user_form': user_form,
                                                 'profile_form': profile_form})
