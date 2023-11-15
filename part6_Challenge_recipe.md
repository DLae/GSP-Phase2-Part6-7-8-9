#Describe the problem:
As a user
So that i can keep track of my music listening
I want to add tracks I've listened to and see a list of them

-------------
#Design Class Interface

class MusicListened():
    def init(self):
        a list for the music
    def add_song(self, song):
        adds song to the list made above
    def output_song_list(self):
        return list of songs
-------------
#Create Test Examples

make sure that we are returning a list = []

check that the list returned is with the right song
make sure that we can add songs to the list

check that the list returned is with the right songs
make sure that we can add songs to the list

the user wants to view an empty list != []
returns/raises  => "Nothing listened to previously"
-------------