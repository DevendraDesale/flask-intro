import os


# Default configs
class BaseConfig(object):
    """
    These are Whole application settings.
    """
    DEBUG = False
    # the key is statically generate and client gets the key then they
    # can regenerate the session, so generate random secret key
    # So use system generated random keys.
    SECRET_KEY = '\xb2\xb8r\xbb`k\xda\xa62qk\x914g\xe6e?~=&EuG9'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


# For different environment we can set different settings
# These classes must extend from base config
class DevelopmentConfig(BaseConfig):
    """
    For the development environment settings.
    """
    DEBUG = True


class ProductionConfig(BaseConfig):
    """
    These are the production configs
    To be aplways explicitly sure define the important configs again.
    """
    DEBUG = True
