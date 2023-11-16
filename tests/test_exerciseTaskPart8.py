from lib.exerciseTaskPart8 import *
import pytest

def sample_diary():
    entry1 = DiaryEntry("Entry 1", "This is the content for the first entry.")
    entry2 = DiaryEntry("Entry 2", "This is the content for the second entry, but this time its a bit longer.")
    diary = Diary()
    diary.add(entry1)
    diary.add(entry2)
    return diary

def test_diary_add():
    diary = Diary()
    entry = DiaryEntry("Test Entry", "Test contents.")
    diary.add(entry)
    assert diary.entries == [entry]
    
def test_diary_count_words():
    assert sample_diary().count_words() == 23
    
def test_diary_reading_time():
    wpm = 200
    assert sample_diary().reading_time(wpm) == pytest.approx(0.1)
    
def test_diary_find_best_entry_for_reading_time():
    wpm = 200
    minutes_available = 5
    best_entry = sample_diary().find_best_entry_for_reading_time(wpm, minutes_available)
    assert best_entry is not None
    assert best_entry.title == "Entry 2"
    
def test_diary_entry_count_words():
    entry = DiaryEntry("Test Entry", "Some test contents here.")
    assert entry.count_words() == 4
    
def test_diary_entry_reading_time():
    entry = DiaryEntry("Test Entry", "Test contents here for now")
    wpm = 200
    assert entry.reading_time(wpm) == pytest.approx(0.025, abs=1e-2)
    
def test_diary_entry_reading_chunk():
    entry = DiaryEntry("Test Title", "Test contents here for now.")
    wpm = 200
    minutes = 2
    chunk1 = entry.reading_chunk(wpm, minutes)
    assert chunk1 == "Test contents here for now."
    