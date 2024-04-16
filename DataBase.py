from sqlalchemy import create_engine, engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv(override=True)
# print(os.environ)
print(os.getenv('DRIVER_NAME'),
      os.getenv('USERNAME'),
      os.getenv('PASSWORD'),
      os.getenv('HOST'),
      os.getenv('DATABASE'),
      os.getenv('PORT'))
database_url = engine.URL.create(drivername=os.getenv('DRIVER_NAME'),
                                 username=os.getenv('USERNAME'),
                                 password=os.getenv('PASSWORD'),
                                 host=os.getenv('HOST'),
                                 database=os.getenv('DATABASE'),
                                 port=os.getenv('PORT'))
print(database_url)

# Create the engine
engine = create_engine(database_url)
print("connection")
Session = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
