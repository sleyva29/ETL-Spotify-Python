import sys
sys.path.append('..')
from views import extract
from views import transform
from views import load

def main(date,username):
    ext = extract.recently_played(date,5)
    trans = transform.filt_art_and_song(ext)
    load.insert_played_songs(username,trans,date)
    return trans
    
if __name__ == '__main__':
    main('2024-03-02','Enrique')
    print('Datos insertados')
    