# Import necessary libraries
import unittest
import json
from unittest.mock import patch
from src import create_app
from src.database import DB

api = create_app()

class TelematicsServiceTestCase(unittest.TestCase):

    def setUp(self):
        api.testing = True
        self.api = api.test_client()
        DB.init(api.config["DB_PATH"], api.config["DB_SCHEMA"])

    def tearDown(self):
        pass

    def test_receive_gps_data(self):
        headers = {'Authorization': 'your_api_token'}
        data = {
            "vehicle_id": "123456",
            "timestamp": "2024-03-26T12:00:00",
            "latitude": 37.7749,
            "longitude": -122.4194
        }
        response = self.api.post('/api/gps', headers=headers, json=data)
        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'], 'GPS data received and saved')

    def test_receive_gps_data_unauthorized(self):
        headers = {'Authorization': 'Bearer invalid_token'}
        data = {
            "vehicle_id": "123456",
            "timestamp": "2024-03-26T12:00:00",
            "latitude": 37.7749,
            "longitude": -122.4194
        }
        response = self.api.post('/api/gps', headers=headers, json=data)
        self.assertEqual(response.status_code, 401)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['error'], 'Unauthorized')

    def test_get_gps_data(self):
        headers = {'Authorization': 'Bearer your_api_token'}
        data = {
            "vehicle_id": "123456",
            "timestamp": "2024-03-26T12:00:00",
            "latitude": 37.7749,
            "longitude": -122.4194
        }
        self.api.post('/api/gps', headers=headers, json=data)

        response = self.api.get('/api/gps/123456')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['gps_data'][0]['vehicle_id'], '123456')

    def test_get_gps_data_not_found(self):
        response = self.api.get('/api/gps/unknown_vehicle_id')
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'], 'No GPS data found for the vehicle')

    @patch('src.health.is_healthy', return_value=True)
    def test_health_check(self, mock_is_healthy):
        response = self.api.get('/health')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['status'], 'Healthy')

if __name__ == '__main__':
    unittest.main()
