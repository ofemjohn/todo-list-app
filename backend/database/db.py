from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db = SQLAlchemy()
load_dotenv()


class Db:
    '''Database connection class to a PostgreSQL database'''

    def __init__(self, app=None):
        self.app = app
        self.db = db

        if app is not None:
            # Set database configuration before initializing SQLAlchemy
            app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
                'DATABASE_URI')
            db.init_app(app)

    def create_all(self):
        '''Create all tables defined in the database models.'''
        with self.app.app_context():
            self.db.create_all()

    def drop_all(self):
        '''Drop all tables defined in the database models.'''
        with self.app.app_context():
            self.db.drop_all()

    def save(self, model_instance):
        '''Save a model instance to the database.'''
        with self.app.app_context():
            self.db.session.add(model_instance)
            self.db.session.commit()

    def delete(self, model_instance):
        '''Delete a model instance from the database.'''
        with self.app.app_context():
            self.db.session.delete(model_instance)
            self.db.session.commit()
