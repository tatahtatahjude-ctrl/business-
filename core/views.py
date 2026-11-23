from django.shortcuts import render

from .forms import ContactForm


def home(request):
	form = ContactForm()
	message_sent = False
	form_name = ""

	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			form_name = form.cleaned_data["name"]
			message_sent = True
			form = ContactForm()

	return render(request, "core/home.html", {
		"form": form,
		"message_sent": message_sent,
		"form_name": form_name,
	})
