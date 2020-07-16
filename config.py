class Config:
    SECRET_KEY ='123456'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:123456@localhost/pomodoro'

    DEBUG=True

config_options = {
    'production': ProdConfig,
    'development' : DevConfig
}
