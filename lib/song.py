class Song:
     # Class attributes to store information about songs
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}
    

    def __init__(self, name, artist, genre):
         # Instance attributes
        self.name= name
        self.artist= artist
        self.genre= genre
        
        # Update class attributes
        Song.count += 1
        Song.genres.add(genre)
        Song.artists.add(artist)
        
        # Update genre_count
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1
        
        # Update artist_count
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1