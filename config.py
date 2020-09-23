import os

class Config():
    
    SECRET_KEY = 'WTF forms secret key'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sandys:Stanford1*@localhost/pitch'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'


    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    
    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    
    DEBUG = True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):

    pass    

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}