from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = os.environ.get('SECRET_KEY', 'portfolio_key')

@app.route('/')
def index():
    perfil = {
        'nome': 'Victor Martins da Silva',
        'titulo': 'Analista de Dados',
        'sobre': 'Engenheiro Agrícola especializado em análise de dados e inovação tecnológica.',
        'email': 'victoreagri@gmail.com',
        'linkedin': 'https://www.linkedin.com/in/victor-martins-da-silva-a111ba190/',
        'github': 'https://github.com/Victormartinsilva'
    }
    return render_template('index.html', perfil=perfil)

@app.route('/backup')
def backup():
    perfil = {
        'nome': 'Victor Martins da Silva',
        'titulo': 'Analista de Dados',
        'sobre': 'Engenheiro Agrícola especializado em análise de dados e inovação tecnológica.',
        'email': 'victoreagri@gmail.com',
        'linkedin': 'https://www.linkedin.com/in/victor-martins-da-silva-a111ba190/',
        'github': 'https://github.com/Victormartinsilva'
    }
    return render_template('index_backup.html', perfil=perfil)

@app.route('/test')
def test():
    return "Flask funcionando no Vercel! ✅"
