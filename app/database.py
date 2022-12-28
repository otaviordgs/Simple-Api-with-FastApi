from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# é o que está na documentação
# fazer as configurações depois !!!
SQLALCHEMY_DATABASE_URL = 'postgresql://otrodrigues:otavio123@localhost:5432/test'
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(
    bind=engine, 
    autocommit=False, 
    autoflush=False
)

# Later we will inherit from this class to 
# create each of the database models or classes
Base = declarative_base()
