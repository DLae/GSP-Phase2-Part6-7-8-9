class MusicListened():
    def __init__(self):
        self.songs = []
    def add_song(self, song):
        self.songs.append(song)
    def output_song_list(self):
        if self.songs == []:
            raise Exception("Nothing listened to previously.")
        return self.songs