import unittest
from fastapi.testclient import TestClient
from backend.main import app


class HealthCheckTestCase(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_health_check(self):
        """Verify that the /api/health endpoint returns HTTP 200 and healthy status."""
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "healthy")
        self.assertIn("anthropic_key_configured", data)


if __name__ == "__main__":
    unittest.main()

