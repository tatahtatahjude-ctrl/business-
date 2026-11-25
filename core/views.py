from django.shortcuts import render

from .forms import ContactForm
from .models import ContactMessage


def home(request):
	form = ContactForm()
	message_sent = False
	form_name = ""

	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			contact_message = form.cleaned_data
			form_name = contact_message["name"]
			ContactMessage.objects.create(**contact_message)
			message_sent = True
			form = ContactForm()

	return render(request, "core/home.html", {
		"form": form,
		"message_sent": message_sent,
		"form_name": form_name,
	})


def services(request):
	return render(request, "core/services.html")
