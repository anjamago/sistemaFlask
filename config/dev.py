
from os.path import abspath, dirname, join


# Define the application directory
BASE_DIR = dirname(dirname(abspath(__file__)))

# Media dir
MEDIA_DIR = join(BASE_DIR, 'media')
POSTS_IMAGES_DIR = join(MEDIA_DIR, 'posts')

SECRET_KEY = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

# Database configuration
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'postgres://girhxuamacdmjr:b9117f7402c6ab1b7a8f0dc6a8ac048561f0de32a66f2d41c92883b8b1f8bbdd@ec2-23-23-36-227.compute-1.amazonaws.com:5432/d6lrqppsaj7t0b'

# App environments
APP_ENV_LOCAL = 'local'
APP_ENV_DEVELOPMENT = 'development'
APP_ENV_STAGING = 'staging'
APP_ENV_PRODUCTION = 'production'
APP_ENV = ''

# Configuración del email
MAIL_SERVER = 'tu servidor smtp'
MAIL_PORT = 587
MAIL_USERNAME = 'tu correo'
MAIL_PASSWORD = 'tu contraseña'
DONT_REPLY_FROM_EMAIL = 'dirección from'
ADMINS = ('juanjo@j2logo.com', )
MAIL_USE_TLS = True
MAIL_DEBUG = False

ITEMS_PER_PAGE = 3