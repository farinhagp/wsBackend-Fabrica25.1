# Meu Projeto Django

Este é um projeto Django simples que implementa um CRUD completo com duas entidades relacionadas: `Usuario` e `Perfil`. O projeto utiliza a API DiceBear para gerar avatares personalizados.

## Funcionalidades

- Cadastro, edição e exclusão de usuários.
- Geração automática de avatares usando a API DiceBear.
- Interface simples e responsiva com HTML e CSS.

## Tecnologias Utilizadas

- **Backend**: Django
- **Banco de Dados**: SQLite (padrão) ou PostgreSQL (opcional)
- **Frontend**: HTML, CSS, Jinja2 (Django Templates)

## Como Executar o Projeto

### Pré-requisitos

- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)

### Passos para Executar

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/farinhagp/wsBackend-Fabrica25.1
   cd meuprojeto
   ```

2. **Crie e ative um ambiente virtual (recomendado):**

   No Linux/MacOS:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   No Windows:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados:**

   O projeto usa SQLite por padrão. Se preferir usar PostgreSQL, atualize as configurações no arquivo `settings.py`:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'meuprojeto',
           'USER': 'user',
           'PASSWORD': 'password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

   Certifique-se de que o PostgreSQL está instalado e em execução.

5. **Aplique as migrações:**

   ```bash
   python manage.py migrate
   ```

6. **Crie um superusuário (opcional):**

   Para acessar o painel de administração do Django, crie um superusuário:

   ```bash
   python manage.py createsuperuser
   ```

   Siga as instruções para definir um nome de usuário, e-mail e senha.

7. **Execute o servidor de desenvolvimento:**

   ```bash
   python manage.py runserver
   ```

8. **Acesse o projeto:**

   Abra o navegador e acesse:

   ```
   http://localhost:8000/
   ```

## Como Contribuir

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Estrutura do Projeto

```
meuprojeto/
├── core/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── meuprojeto/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
```

## Configuração para Produção

Para implantar o projeto em produção, siga estas etapas:

1. Defina `DEBUG=False` no arquivo `settings.py`.

2. Configure um servidor web como Nginx ou Apache para servir o projeto.

3. Use o Gunicorn como servidor de aplicação:

   ```bash
   pip install gunicorn
   gunicorn meuprojeto.wsgi:application --bind 0.0.0.0:8000
   ```

4. Use o Whitenoise para servir arquivos estáticos:

   No `settings.py`, adicione:

   ```python
   MIDDLEWARE = [
       ...
       'whitenoise.middleware.WhiteNoiseMiddleware',
       ...
   ]

   STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
   ```

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.

## Contato

Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato:

- **Nome**: Thiago
- **Email**: [tiagovictor674@gmail.com](mailto\:thiagovictor674@gmail.com)
- **GitHub**: Thiago-Victor

---
