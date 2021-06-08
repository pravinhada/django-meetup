from django.shortcuts import redirect, render

from .models import Meetup, Participant
from .forms import RegistrationForm
# Create your views here.


def index(request):
    meetups = Meetup.objects.all()
    context = {
        'show_meetups': True,
        'meetups': meetups
    }
    return render(request, "meetups/index.html", context)


def meetup_details(request, slug):
    try:
        selected_meetup = Meetup.objects.get(slug=slug)

        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(
                    email=user_email)
                selected_meetup.participants.add(participant)
                return redirect("confirm-registration", slug=slug)

        return render(request, "meetups/meetup-details.html", {
            'meetup_found': True,
            'meetup': selected_meetup,
            'form': registration_form
        })
    except Exception as exc:
        return render(request,  "meetups/meetup-details.html", {
            'meetup_found': False
        })


def confirm_registration(request, slug):
    meetup = Meetup.objects.get(slug=slug)
    return render(request, "meetups/registration-success.html", {'meetup': meetup})
