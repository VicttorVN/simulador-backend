import os
from pathlib import Path

# 🔧 Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# 🛡️ Segurança
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'troque-esta-chave-urgentemente')
DEBUG = True
ALLOWED_HOSTS = ['*']  # Em produção, especifique os domínios permitidos

# 📦 Aplicações instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Libs externas
    'rest_framework',
    'corsheaders',

    # App do projeto
    'simulador',
]

# 🔄 Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # ← CORS deve vir antes de SessionMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🌐 Rotas
ROOT_URLCONF = 'core.urls'

# 🎨 Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Pode incluir: [BASE_DIR / 'templates']
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 🚀 WSGI
WSGI_APPLICATION = 'core.wsgi.application'

# 🗃️ Banco de dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 🔐 Validações de senha
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator' },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator' },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator' },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator' },
]

# 🌎 Internacionalização
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Cuiaba'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# 📁 Arquivos estáticos
STATIC_URL = '/static/'

# 🔧 Configuração padrão para campos auto incrementais
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 🌐 CORS
CORS_ALLOW_ALL_ORIGINS = True  # Apenas em desenvolvimento, cuidado em produção