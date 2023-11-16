class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.words = contents.split()

    def count_words(self):
        return len(self.words)

    def reading_time(self, wpm):
        return len(self.words) / wpm

    def reading_chunk(self, wpm, minutes):
        words_to_read = wpm * minutes
        chunk = ' '.join(self.words[:words_to_read])
        self.words = self.words[words_to_read:]
        return chunk


class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        self.entries.append(entry)

    def all(self):
        return self.entries

    def count_words(self):
        return sum(entry.count_words() for entry in self.entries)

    def reading_time(self, wpm):
        return round(sum(entry.reading_time(wpm) for entry in self.entries),1)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        entries = sorted(self.entries, key=lambda x: abs(x.reading_time(wpm) - minutes))
        for entry in entries:
            if entry.reading_time(wpm) <= minutes:
                return entry
        return None