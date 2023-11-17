import unittest
from datetime import datetime
from lib.Part9Exercise import Diary, DiaryEntry, TodoList, ContactManager

class TestDiary(unittest.TestCase):

    def test_add_entry_and_get_entries(self):
        diary = Diary()
        entry = DiaryEntry(date=datetime.now(), entry_text="Today was a good day.")
        diary.add_entry(entry)
        entries = diary.get_entries()
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0], entry)

    def test_get_entries_by_time_and_speed(self):
        diary = Diary()
        entry1 = DiaryEntry(date=datetime.now(), entry_text="Morning entry.", time="morning", speed="fast")
        entry2 = DiaryEntry(date=datetime.now(), entry_text="Evening entry.", time="evening", speed="slow")
        diary.add_entry(entry1)
        diary.add_entry(entry2)

        selected_entries = diary.get_entries_by_time_and_speed(time="morning", speed="fast")
        self.assertEqual(len(selected_entries), 1)
        self.assertEqual(selected_entries[0], entry1)

    def test_add_task_to_diary_entry(self):
        entry = DiaryEntry(date=datetime.now(), entry_text="Today was a good day.")
        todo_list = TodoList()
        todo_list.add_task("Finish work project")
        entry.add_task_list(todo_list)
        self.assertEqual(entry.get_task_list(), todo_list)

    def test_get_phone_numbers_from_diary_entries(self):
        diary = Diary()
        entry1 = DiaryEntry(date=datetime.now(), entry_text="Met John today. His number is 123-456-7890.")
        entry2 = DiaryEntry(date=datetime.now(), entry_text="Called Mary at 987-654-3210.")
        diary.add_entry(entry1)
        diary.add_entry(entry2)

        contact_manager = ContactManager()
        contact_manager.extract_phone_numbers(diary.get_entries())
        phone_numbers = contact_manager.get_phone_numbers()
        self.assertIn("123-456-7890", phone_numbers)
        self.assertIn("987-654-3210", phone_numbers)

if __name__ == '__main__':
    unittest.main()