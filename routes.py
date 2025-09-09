import unittest
from main import app
from flask import render_template

class TestSite(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Bem-vindo ao site sobre cachorros!', response.data)

    def test_border_page(self):
        response = self.app.get('/border')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Border Collie', response.data) 


