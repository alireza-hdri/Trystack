from os import environ

class config : 
    ENV = environ.get("TRYSATCK_API_ENV", "production")
    DEBUG = bool(int(environ.get("TRYSTACK_API_DEBUG" , "0")))
    TESTING = DEBUG