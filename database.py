from sqlalchemy import create_engine, Column,Integer, String, Float,ForeignKey
from sqlalchemy.orm import sessionmaker,declarative_base

import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')
db_name = os.getenv('POSTGRES_DB')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')

DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind = engine)

Base = declarative_base()

class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, index = True)
    titulo = Column(String, nullable=True)
    descricao = Column(String)
    preco = Column(Float, nullable=False)