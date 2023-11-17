from datetime import datetime

class DiaryEntry:
    def __init__(self, date, entry_text, time=None, speed=None):
        self.date = date
        self.entry_text = entry_text
        self.time = time
        self.speed = speed
        self.task_list = None

    def add_task_list(self, task_list):
        self.task_list = task_list

    def get_task_list(self):
        return self.task_list

class Diary:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def get_entries(self):
        return self.entries

    def get_entries_by_time_and_speed(self, time, speed):
        selected_entries = [entry for entry in self.entries if entry.time == time and entry.speed == speed]
        return selected_entries

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks

class ContactManager:
    def __init__(self):
        self.phone_numbers = set()

    def extract_phone_numbers(self, entries):
        for entry in entries:
            # Simple phone number extraction (you may need a more robust solution)
            words = entry.entry_text.split()
            for word in words:
                if "-" in word and word.replace("-", "").isdigit():
                    self.phone_numbers.add(word)

    def get_phone_numbers(self):
        return list(self.phone_numbers)