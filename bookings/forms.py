from django import forms
from django.utils import timezone

from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ("name", "email", "requested_date", "notes")
        widgets = {
            "requested_date": forms.DateInput(attrs={"type": "date"}),
            "notes": forms.Textarea(attrs={"rows": 4}),
        }

    def clean_requested_date(self):
        requested_date = self.cleaned_data["requested_date"]
        if requested_date < timezone.localdate():
            raise forms.ValidationError("Choose today or a future date.")
        return requested_date
