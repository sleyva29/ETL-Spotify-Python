from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, DateTime, text
from sqlalchemy.dialects.mysql import JSON
from sqlalchemy import create_engine
import os

user=os.environ['MYSQL_USERNAME']
password=os.environ['MYSQL_PASSWORD']
host = os.environ['MYSQL_HOST']

class Base(DeclarativeBase):
    id = Column('id', Integer, primary_key=True)
    created_at = Column("created_at", DateTime, nullable=False, server_default=text("now()"))
    updated_at = Column("updated_at", DateTime, nullable=False, server_default=text("now()"))

class PlayedSong(Base):
    __tablename__ = "played_songs"
    
    username = Column("username",String(100), nullable=False)
    songs = Column("songs",JSON, nullable=False)
    played_at = Column("played_at", DateTime, nullable=False)
    

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/etl-spotify')

Base.metadata.create_all(engine)
 
  
    