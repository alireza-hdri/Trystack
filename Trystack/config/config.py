from os import environ

class config : 
    ENV = environ.get("TRYSATCK_API_ENV", "production")
