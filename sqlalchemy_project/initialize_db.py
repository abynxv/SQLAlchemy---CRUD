from crud_app.sqlalchemy_config import engine, Base
from crud_app.models import College, Student


Base.metadata.create_all(bind=engine)