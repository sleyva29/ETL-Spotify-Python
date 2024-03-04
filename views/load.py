import sqlalchemy as db
from sqlalchemy import insert
import os

user=os.environ['MYSQL_USERNAME']
password=os.environ['MYSQL_PASSWORD']
host = os.environ['MYSQL_HOST']

# Create an engine to connect to the database
engine = db.create_engine(f'mysql+pymysql://{user}:{password}@{host}/etl-spotify')
metadata = db.MetaData()

# Create a connection to the engine
def insert_played_songs(username, songs, played_at):
    connection = engine.connect()
    
    played_songs = db.Table('played_songs', metadata, autoload_with=engine)
    query = insert(played_songs).values(username = username, songs = songs, played_at = played_at)
    connection.execute(query)
    connection.commit()
    connection.close()
    

if __name__ == '__main__':
    insert_played_songs("Enrique", [{'artist': 'Carlos Rivera', 'song': 'Un Viaje a Todas Partes'}], "2024-03-03")
    print('Datos insertados')
    


