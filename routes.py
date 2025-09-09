from main import app
from flask import render_template

# rotas
@app.route('/')
def home():
    return render_template('home.html')

#pagina sobre cachorros
@app.route('/border')
def border():
    return render_template('border.html')


