from django.shortcuts import render

from .forms import BookingForm


def booking_request(request):
    form = BookingForm()
    submitted = False

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
            form = BookingForm()

    return render(request, "bookings/booking_form.html", {
        "form": form,
        "submitted": submitted,
    })
