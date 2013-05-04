from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Model = declarative_base(name='Model')


def get_session(app):
    if not hasattr(app, 'db_session'):
        # Create the engine
        engine = create_engine(app.config.get('DATABASE_URL'),
                               convert_unicode=True)

        # Create a session
        Session = sessionmaker(bind=engine, autocommit=False,
                               autoflush=False)
        app.db_session = Session()

    return app.db_session
