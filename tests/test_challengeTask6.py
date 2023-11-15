from lib.challengeTask6 import *
import pytest
    
def test_check_to_see_return_list_with_correct_song():
    music_list = MusicListened()
    music_list.add_song("Disconnect")
    assert music_list.output_song_list() == ["Disconnect"]
    
def test_check_to_see_return_list_with_correct_songs():
    music_list = MusicListened()
    music_list.add_song("Disconnect")
    music_list.add_song("Gold Dust")
    music_list.add_song("Shut up and Drive")
    assert music_list.output_song_list() == ["Disconnect", "Gold Dust", "Shut up and Drive"]
    
def test_check_to_see_raise_error_message_when_list_empty():
    music_list = MusicListened()
    with pytest.raises(Exception) as e:
        music_list.output_song_list()
    assert str(e.value) == "Nothing listened to previously."