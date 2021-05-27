from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_animal(self):
        response = self.client.get(url_for("animals"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.data.decode('utf-8'), ['cow','horse','pig'])

    def test_get_noise(self):
        test_cases = [('cow','moo'),('horse','neigh'),('pig','oink')]
        for case in test_cases:
            response = self.client.post(url_for("noises"), data=case[0])
            self.assertEqual(response.status_code, 200)
            self.assertEqual(case[1],response.data.decode('utf-8'))