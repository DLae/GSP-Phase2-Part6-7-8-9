Describe the Problem:
As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

-------------
Design Class System:


-------------
Create Test Examples:

# Example Unit Test for DiaryEntry
def test_diary_entry_add_task():
    entry = DiaryEntry(date="2023-11-17", entry_text="Today was a good day.")
    entry.add_task("Finish work project")
    assert entry.get_entry_text() == "Today was a good day.\nTasks: Finish work project"
# Example Unit Test for Diary
def test_diary_get_entries_by_time_and_speed():
    diary = Diary()
    entry1 = DiaryEntry(date="2023-11-17", entry_text="Today was a good day.")
    entry2 = DiaryEntry(date="2023-11-18", entry_text="Another day.")
    diary.add_entry(entry1)
    diary.add_entry(entry2)
    result = diary.get_entries_by_time_and_speed("morning", "fast")
    assert result == [entry1]

    ^^^
    these tests can be performed for each function within the classes
    would just need to change what class/function youre calling