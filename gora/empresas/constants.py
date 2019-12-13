APP_ROOT_PATH = "empresas/"

######
# PAGE TITLES
LOGIN_TITLE = "Login"
INDEX_TITLE = ""
ACCOUNT_TITLE = "Mi cuenta"

###########
# URLS
LOGIN_URL = "/" + APP_ROOT_PATH + "login"
ACCOUNT_URL = "/" + APP_ROOT_PATH + "account"
INDEX_URL = "/" + APP_ROOT_PATH


###########
# TEMPLATES
LOGIN_TEMPLATE = APP_ROOT_PATH + "login.html"
INDEX_TEMPLATE = APP_ROOT_PATH + "index.html"
ACCOUNT_TEMPLATE = APP_ROOT_PATH + "account.html"


###########
# MESSAGES
LOGIN_MESSAGE_ERROR = 'Email y/o contraseña inváldos.'
CHANGE_PASSWORD_MESSAGE_ERROR = 'Contraseña inválda.'
CHANGE_PASSWORD_NOT_MATCH_MESSAGE_ERROR = 'Contraseñas no coinciden.'

