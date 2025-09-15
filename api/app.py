from flask import Flask, render_template, send_from_directory, request, flash, redirect, url_for
from flask_compress import Compress
import os
from datetime import datetime

# Criação da instância da aplicação Flask
app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = os.environ.get('SECRET_KEY', 'portfolio_victor_2024')

# Configurações de produção
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 31536000
Compress(app)

# Headers de segurança
@app.after_request
def after_request(response):
    if request.endpoint == 'static' or request.endpoint == 'assets':
        response.cache_control.max_age = 31536000
        response.cache_control.public = True
    
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    
    return response

# Rota principal - página inicial (versão gamificada)
@app.route('/')
def index():
    # Dados do perfil pessoal
    perfil = {
        'nome': 'Victor Martins da Silva',
        'titulo': 'Analista de Dados',
        'sobre': 'Engenheiro Agrícola especializado em análise de dados e inovação tecnológica. Experiência em projetos de análise geoestatística, automação de processos e desenvolvimento de dashboards. Competente em Python, R e ferramentas de BI como Power BI e Tableau.',
        'localizacao': 'São Paulo - SP',
        'telefone': '(45) 99922-5862',
        'email': 'victoreagri@gmail.com',
        'github': 'https://github.com/Victormartinsilva',
        'linkedin': 'https://www.linkedin.com/in/victor-martins-da-silva-a111ba190/',
        'whatsapp': 'https://wa.me/5545999225862'
    }
    
    # Experiências profissionais
    experiencias = [
        {
            'empresa': 'EICON',
            'cargo': 'Analista de Dados',
            'periodo': 'Out 2024 - Presente',
            'descricao': 'Análise de dados para identificar oportunidades e tendências de mercado. Desenvolvimento de relatórios e dashboards para apoio à tomada de decisão estratégica.',
            'icone': '📊'
        },
        {
            'empresa': 'Unimaq - John Deere',
            'cargo': 'Analista de Agricultura de Precisão',
            'periodo': 'Out 2023 - Out 2024',
            'descricao': 'Suporte técnico especializado em agricultura de precisão, análise de dados agrícolas e desenvolvimento de soluções tecnológicas para otimização da produtividade.',
            'icone': '🚜'
        },
        {
            'empresa': 'FK Steel',
            'cargo': 'Auxiliar de PCP',
            'periodo': 'Fev 2023 - Jun 2023',
            'descricao': 'Programação CNC, controle de produção e criação de dashboards para análise de custos, produtividade e otimização de processos produtivos.',
            'icone': '🏭'
        },
        {
            'empresa': 'FK Steel',
            'cargo': 'Estagiário de Projetos',
            'periodo': 'Out 2022 - Fev 2023',
            'descricao': 'Desenvolvimento de projetos de equipamentos metálicos em SolidWorks, detalhamento técnico e elaboração de documentação para fabricação.',
            'icone': '🔧'
        },
        {
            'empresa': 'CNPq',
            'cargo': 'Pesquisador Científico',
            'periodo': 'Ago 2017 - Mai 2019',
            'descricao': 'Pesquisa em análise geoestatística de variáveis georreferenciadas utilizando R, MySQL e QGIS. Desenvolvimento de mapas temáticos e dashboards analíticos.',
            'icone': '🔬'
        }
    ]
    
    # Educação
    educacao = [
        {
            'instituicao': 'UNIOESTE',
            'curso': 'Engenharia Agrícola',
            'periodo': '2017 - 2023',
            'tipo': 'Graduação'
        },
        {
            'instituicao': 'FAMEEF',
            'curso': 'Engenharia de Software',
            'periodo': '2024 - Presente',
            'tipo': 'Pós-graduação'
        }
    ]
    
    # Competências organizadas por categoria
    competencias = {
        'analise_dados': {
            'nome': 'Análise de Dados',
            'skills': ['Python', 'R', 'Power BI', 'Tableau', 'Excel', 'MySQL', 'QGIS']
        },
        'programacao': {
            'nome': 'Programação',
            'skills': ['Python', 'C', 'R']
        },
        'ferramentas': {
            'nome': 'Ferramentas Técnicas',
            'skills': ['AutoCAD', 'SolidWorks', 'SketchUp', 'Lumens', 'Ftool', 'Visualventos']
        },
        'metodologias': {
            'nome': 'Metodologias',
            'skills': ['SCRUM', 'BPMN', '5S', 'PDCA', '5W2H']
        }
    }
    
    # Idiomas
    idiomas = {
        'ingles': {'nome': 'Inglês', 'nivel': 'Intermediário', 'porcentagem': 70},
        'espanhol': {'nome': 'Espanhol', 'nivel': 'Básico', 'porcentagem': 40}
    }
    
    # Certificações
    certificacoes = [
        {'nome': 'Power BI', 'instituicao': 'Alura', 'ano': '2023'},
        {'nome': 'Python', 'instituicao': 'Alura', 'ano': '2023'},
        {'nome': 'SCRUM', 'instituicao': 'Alura', 'ano': '2023'},
        {'nome': 'BPMN', 'instituicao': 'Alura', 'ano': '2023'}
    ]
    
    # Projetos
    projetos = [
        {
            'nome': 'Sistema de Análise Geoestatística',
            'descricao': 'Desenvolvimento de sistema para análise espacial de dados agrícolas utilizando R, MySQL e QGIS.',
            'tecnologias': ['R', 'MySQL', 'QGIS'],
            'github': 'https://github.com/Victormartinsilva'
        },
        {
            'nome': 'Dashboard de Controle de Produção',
            'descricao': 'Criação de dashboards para monitoramento de KPIs de produção industrial.',
            'tecnologias': ['Power BI', 'Excel'],
            'github': 'https://github.com/Victormartinsilva'
        },
        {
            'nome': 'Portfólio Interativo',
            'descricao': 'Desenvolvimento de portfólio pessoal com design gamificado e visualizações interativas.',
            'tecnologias': ['Python', 'Flask', 'D3.js'],
            'github': 'https://github.com/Victormartinsilva/victor-portfolio-working'
        }
    ]
    
    return render_template('index.html', 
                         perfil=perfil,
                         experiencias=experiencias,
                         educacao=educacao,
                         competencias=competencias,
                         idiomas=idiomas,
                         certificacoes=certificacoes,
                         projetos=projetos)

# Rota para a versão backup (layout tradicional)
@app.route('/backup')
def backup():
    # Mesmos dados da rota principal
    perfil = {
        'nome': 'Victor Martins da Silva',
        'titulo': 'Analista de Dados',
        'sobre': 'Engenheiro Agrícola especializado em análise de dados e inovação tecnológica. Experiência em projetos de análise geoestatística, automação de processos e desenvolvimento de dashboards. Competente em Python, R e ferramentas de BI como Power BI e Tableau.',
        'localizacao': 'São Paulo - SP',
        'telefone': '(45) 99922-5862',
        'email': 'victoreagri@gmail.com',
        'github': 'https://github.com/Victormartinsilva',
        'linkedin': 'https://www.linkedin.com/in/victor-martins-da-silva-a111ba190/',
        'whatsapp': 'https://wa.me/5545999225862'
    }
    
    experiencias = [
        {
            'empresa': 'EICON',
            'cargo': 'Analista de Dados',
            'periodo': 'Out 2024 - Presente',
            'descricao': 'Análise de dados para identificar oportunidades e tendências de mercado. Desenvolvimento de relatórios e dashboards para apoio à tomada de decisão estratégica.',
            'icone': '📊'
        },
        {
            'empresa': 'Unimaq - John Deere',
            'cargo': 'Analista de Agricultura de Precisão',
            'periodo': 'Out 2023 - Out 2024',
            'descricao': 'Suporte técnico especializado em agricultura de precisão, análise de dados agrícolas e desenvolvimento de soluções tecnológicas para otimização da produtividade.',
            'icone': '🚜'
        }
    ]
    
    educacao = [
        {
            'instituicao': 'UNIOESTE',
            'curso': 'Engenharia Agrícola',
            'periodo': '2017 - 2023',
            'tipo': 'Graduação'
        },
        {
            'instituicao': 'FAMEEF',
            'curso': 'Engenharia de Software',
            'periodo': '2024 - Presente',
            'tipo': 'Pós-graduação'
        }
    ]
    
    competencias = {
        'analise_dados': {
            'nome': 'Análise de Dados',
            'skills': ['Python', 'R', 'Power BI', 'Tableau', 'Excel', 'MySQL', 'QGIS']
        },
        'programacao': {
            'nome': 'Programação',
            'skills': ['Python', 'C', 'R']
        }
    }
    
    idiomas = {
        'ingles': {'nome': 'Inglês', 'nivel': 'Intermediário', 'porcentagem': 70},
        'espanhol': {'nome': 'Espanhol', 'nivel': 'Básico', 'porcentagem': 40}
    }
    
    certificacoes = [
        {'nome': 'Power BI', 'instituicao': 'Alura', 'ano': '2023'},
        {'nome': 'Python', 'instituicao': 'Alura', 'ano': '2023'}
    ]
    
    projetos = [
        {
            'nome': 'Sistema de Análise Geoestatística',
            'descricao': 'Desenvolvimento de sistema para análise espacial de dados agrícolas utilizando R, MySQL e QGIS.',
            'tecnologias': ['R', 'MySQL', 'QGIS'],
            'github': 'https://github.com/Victormartinsilva'
        }
    ]
    
    return render_template('index_backup.html',
                         perfil=perfil,
                         experiencias=experiencias,
                         educacao=educacao,
                         competencias=competencias,
                         idiomas=idiomas,
                         certificacoes=certificacoes,
                         projetos=projetos)

# Rota para processar o formulário de contato
@app.route('/contato', methods=['POST'])
def contato():
    nome = request.form.get('nome')
    email = request.form.get('email')
    mensagem = request.form.get('mensagem')
    
    if nome and email and mensagem:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        contato_info = f"\n--- NOVO CONTATO [{timestamp}] ---\n"
        contato_info += f"Nome: {nome}\n"
        contato_info += f"Email: {email}\n"
        contato_info += f"Mensagem: {mensagem}\n"
        contato_info += "-" * 40 + "\n"
        
        try:
            with open('contatos.txt', 'a', encoding='utf-8') as f:
                f.write(contato_info)
            flash('Mensagem enviada com sucesso! Entrarei em contato em breve.', 'success')
        except Exception as e:
            flash('Erro ao enviar mensagem. Tente novamente.', 'error')
    else:
        flash('Por favor, preencha todos os campos.', 'error')
    
    return redirect(url_for('index'))

@app.route('/test')
def test():
    return "✅ Flask funcionando perfeitamente no Vercel!"

# Rota para servir arquivos estáticos (CSS, JS, imagens)
@app.route('/<path:filename>')
def assets(filename):
    return send_from_directory('..', filename)
