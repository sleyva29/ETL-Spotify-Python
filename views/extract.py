import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import datetime
import pandas as pd
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

scope = "user-read-recently-played"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ['SPOTIPY_CLIENT_ID'],
                                                client_secret=os.environ['SPOTIPY_CLIENT_SECRET'],
                                                redirect_uri=os.environ['SPOTIPY_REDIRECT_URI'],
                                                scope=scope))

def recently_played(date: str,limit: int = 1):    
    dt = datetime.datetime.strptime(date, "%Y-%m-%d")
    timestamp = int(dt.timestamp() * 1000)
    result = sp.current_user_recently_played(limit=limit, after=timestamp)
    
    if result['next']:
        print('Quedan datos pendientes')
        
    result = result['items']
    
    res = pd.DataFrame(result)
    res['played_at'] = pd.to_datetime(res['played_at'])
    
    result = res[res['played_at'].dt.date == dt.date()].to_dict('records')
    
    return result
    
if __name__ == '__main__':
    print(recently_played('2024-03-02',5))   
