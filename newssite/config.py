from dotenv import load_dotenv


load_dotenv()


class Config:
    TESTING = False


class DevConfig(Config):
    TESTING = False
    DEBUG = True
    ENV = 'development'


class ProdConfig(Config):
    TESTING = False
    DEBUG = False
    ENV = 'production'


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    ENV = 'development'
