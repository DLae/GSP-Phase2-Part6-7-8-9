class TaskTracker():
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def list_incomplete(self):
        return self.tasks

    def mark_complete(self, index):
        if index >= len(self.tasks) or index < 0:
            raise Exception("Task doesn't exist")
        self.tasks.pop(index)