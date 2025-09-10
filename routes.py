import os
import unittest
from flask import Flask, render_template
from main import app

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

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

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)