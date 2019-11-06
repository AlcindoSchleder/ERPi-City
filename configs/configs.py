# Configuração da base de dados
# Exemplo: DEFAULT_DATABASE_URL = 'db_multi'
# Caso seja deixado vazio o default será: 'sqlite:////...djangosige/db.sqlite3'
APP_DBMODE_SINGLE_DATABASE = 'single_db'
APP_DBMODE_MULTI_DATABASES = 'multi_db'
APP_DBMODE_MULTI_SCHEMAS = 'multi_sh'

APP_DBMODES = {
    APP_DBMODE_SINGLE_DATABASE: 'Banco de Dados Único',
    APP_DBMODE_MULTI_DATABASES: 'Banco de Dados por Empresa',
    APP_DBMODE_MULTI_SCHEMAS: 'Banco de Dados com Esquemas Isolados por Empresa'
}

APP_DBMODES_CHOICES = [
    (APP_DBMODE_SINGLE_DATABASE, APP_DBMODES[APP_DBMODE_SINGLE_DATABASE]),
    (APP_DBMODE_MULTI_DATABASES, APP_DBMODES[APP_DBMODE_MULTI_DATABASES]),
    (APP_DBMODE_MULTI_SCHEMAS, APP_DBMODES[APP_DBMODE_MULTI_SCHEMAS]),
]

DEFAULT_DATABASE_MODE = APP_DBMODE_MULTI_DATABASES

# Configuração da base de dados
# Exemplo: DEFAULT_DATABASE_URL = 'postgres://user:pass@localhost/dbname'
# Caso seja deixado vazio o default será: 'sqlite:////...djangosige/db.sqlite3'
DEFAULT_DATABASE_URL = ''

#
# Configurações do servidor de email
# Obs: Por enquanto o endereço de email é utilizado apenas para a troca de senha do usuário.
# Endereço de email padrão utilizado
#
DEFAULT_FROM_EMAIL = ''

EMAIL_HOST = 'smtp.gmail.com'  # Gmail
# EMAIL_HOST = 'smtp.live.com' #Hotmail

# Usuário do email padrão
EMAIL_HOST_USER = ''

# Senha do email padrão
EMAIL_HOST_PASSWORD = ''

# Verificar a port utilizada pelo serviço de email
EMAIL_PORT = 587

EMAIL_USE_TLS = True
