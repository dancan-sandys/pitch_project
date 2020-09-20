class Config():
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sandys:Stanford1*@localhost/pitch'
    
    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    
    DEBUG = True

class ProdConfig(Config):
    pass

class TestConfig(Config):

    pass    

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}