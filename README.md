# Navalha & Prosa - Site da Barbearia

Projeto em Django com tela de login conectada à página institucional da barbearia, usando templates, arquivos estáticos e `{% url %}`.

## Tecnologias
Python, Django, HTML5, CSS3

## Como rodar
1. Crie e ative o ambiente virtual: `python -m venv venv` e `.\venv\Scripts\Activate.ps1`
2. Instale as dependências: `pip install -r requirements.txt`
3. Inicie o servidor: `python manage.py runserver`
4. Acesse http://127.0.0.1:8000

## Estrutura
- `cadastro/`: app com views, urls, templates e arquivos estáticos
- `sistema/`: configurações do projeto'