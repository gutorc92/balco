import unittest
import json
import urllib.request
from flask_testing import TestCase
import sys
sys.path.append('..')
from api import app

class MyTest(TestCase):

	def create_app(self):
		app.config['TESTING'] = True
		# app.config['LIVESERVER_PORT'] = 8943
		# # Default timeout is 5 seconds
		# app.config['LIVESERVER_TIMEOUT'] = 10
		return app
	
	def test_post(self):
		data = {
			'array': [3, 4, 1, 7, 8, 5],
			'K': 2,
			'L': 3
		}
		with self.app.test_client() as c:
			response = c.post('/calculate', json=data)
			self.assertEqual(response.status_code, 200)
			result = response.get_json()
			self.assertEqual(result['total'], 27)
	
	def test_wrong_data(self):
		data = {
			'K': 2,
			'L': 3
		}
		with self.app.test_client() as c:
			response = c.post('/calculate', json=data)
			self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
	unittest.main()