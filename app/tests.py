from django.test import TestCase


class HealthcheckTests(TestCase):
	def test_healthcheck_returns_ok(self):
		response = self.client.get('/health/')

		self.assertEqual(response.status_code, 200)
		self.assertJSONEqual(response.content, {'status': 'ok'})
