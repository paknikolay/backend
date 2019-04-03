import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'strong-password'

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@postgres:5432/postgres'#'sqlite:///' + os.path.join(basedir, 'app.db')#
 # or \

#os.environ.get('DATABASE_URL') 
  #    SQLALCHEMY_TRACK_MODIFICATIONS = False

   

    # mail settings
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    # gmail authentication
    MAIL_USERNAME = 'pak.nick.al@gmail.com'
    MAIL_PASSWORD = 'kolya4247'

    # mail accounts
    MAIL_DEFAULT_SENDER = 'pak.nick.al@gmail.com'


