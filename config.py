"""
Flask configuration class for production,
development, and testing
"""

class Config(object):

    DEBUG = False
    TESTING = False

    DB_NAME = "production_db"
    DB_PASSWORD ="this will change later"
    UPLOADS = "./app/static/uploads"
    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    DB_NAME = "development_db"
    DB_PASSWORD = "change_this_later"
    UPLOADS = "/flask_test/uploads"
    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True
    DB_NAME = "development_db"
    DB_PASSWORD = "change_this_later"
    UPLOADS = "/flask_test/uploads"
    SESSION_COOKIE_SECURE = False
