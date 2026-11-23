from django.test import TestCase


class HomePageTests(TestCase):
	def test_homepage_loads(self):
		response = self.client.get("/")

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Your Business")
		self.assertContains(response, "Services")

	def test_contact_form_accepts_valid_submission(self):
		response = self.client.post("/", {
			"name": "Alex",
			"email": "alex@example.com",
			"message": "I would like to learn more about your services.",
		})

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Thanks, Alex")

	def test_contact_form_rejects_invalid_submission(self):
		response = self.client.post("/", {
			"name": "",
			"email": "not-an-email",
			"message": "",
		})

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "This field is required")
