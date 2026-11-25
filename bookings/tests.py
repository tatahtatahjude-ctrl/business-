from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from .models import Booking


class BookingTests(TestCase):
    def test_booking_page_loads(self):
        response = self.client.get("/bookings/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Request a booking")

    def test_valid_booking_is_saved(self):
        requested_date = timezone.localdate() + timedelta(days=7)
        response = self.client.post("/bookings/", {
            "name": "Alex",
            "email": "alex@example.com",
            "requested_date": requested_date,
            "notes": "Please call before the appointment.",
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your booking request has been received")
        self.assertEqual(Booking.objects.count(), 1)

    def test_past_booking_is_rejected(self):
        requested_date = timezone.localdate() - timedelta(days=1)
        response = self.client.post("/bookings/", {
            "name": "Alex",
            "email": "alex@example.com",
            "requested_date": requested_date,
            "notes": "",
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Choose today or a future date")
        self.assertEqual(Booking.objects.count(), 0)
