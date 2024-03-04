import extract
import transform
import load

def main(date,username):
    ext = extract.recently_played(date,5)
    trans = transform.filt_art_and_song(ext)
    load.insert_played_songs(username,trans,date)
    
if __name__ == '__main__':
    main('2024-03-02','Enrique')
    print('Datos insertados')
    