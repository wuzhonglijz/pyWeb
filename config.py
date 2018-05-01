class Config(object):
    """Base config class."""
    pass

class ProdConfig(Config):
    """Production config class."""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/prod.db'

class DevConfig(Config):
    """Development config class."""
    # Open the DEBUG
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/test.db'

class DatabaseConfig(Config):
    #
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True