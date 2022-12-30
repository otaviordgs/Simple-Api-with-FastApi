from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#A documentação do fastapi recomenda esse arquivo ser dessa maneira

#Exemplo: SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
#A variavel é db, pois quando usa-se o docker-compose, da maneira que foi usada (com depends on na parte do build api), é criado um network
#para que os containers desse arquivo conversem entre si. E o nome desse arquivo é db, para mais informações: https://docs.docker.com/compose/networking/

SQLALCHEMY_DATABASE_URL = 'postgresql://admin:password@db:5432/test'


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(
    bind=engine, 
    autocommit=False, 
    autoflush=False
)

#Usamos essa variavel para representar as tabelas em classes, usadas no arquivo models.py
Base = declarative_base()
