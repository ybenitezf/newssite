from dotenv import load_dotenv
import os


load_dotenv()


class Config:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', None)


class DevConfig(Config):
    TESTING = False
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'


class ProdConfig(Config):
    TESTING = False
    DEBUG = False
    ENV = 'production'

class TestConfig(Config):
    TESTING = True
    DEBUG = True
    ENV = 'development'
