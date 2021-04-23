from password import mysql_password

class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql://root:" + mysql_password + "@localhost:3306/pop"
    SQLALCHEMY_TRACK_MODIFICATIONS = False