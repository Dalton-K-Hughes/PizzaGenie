import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    config_type = os.getenv('FLASK_CONFIG', 'development')
    
    if config_type == 'production':
        app.config.from_object('website.config.ProductionConfig')
    elif config_type == 'testing':
        app.config.from_object('website.config.TestingConfig')
    else:
        app.config.from_object('website.config.DevelopmentConfig')
        
    db.init_app(app)
    
    
    
    from .views import views
    
    app.register_blueprint(views, url_prefix='/')
    
    return app