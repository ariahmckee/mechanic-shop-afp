
class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:<YOUR MYSQL PASSWORD>@localhost/<YOUR DATABASE>'
    DEBUG = True

DevelopementConfig = DevelopmentConfig
    
class TestingConfig:
    pass

class ProductionConfig:
    pass
