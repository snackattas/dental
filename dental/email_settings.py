import os
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('HOST_EMAIL')
EMAIL_HOST_PASSWORD = os.environ.get('HOST_EMAIL_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_TIMEOUT = 10