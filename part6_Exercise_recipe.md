##Describe the Problem:
As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

-------------
##Design the Class Interface:

class TaskTracker():
    def _init__(self):
        pass
    def add(self, task):
        task : string
    def list_incomplete(self):
        return : list of tasks
    def mark_complete(self, index):
        task : int - relates to tasks position in list
        what it does : removes the task from the list

-------------
##Create Examples as Tests:

tracker = TaskTracker()
assert tracker.list_incomplete() == []

tracker = TaskTracker()
tracker.add("Walk dog")
assert tracker.list_incomplete() == ["Walk dog"]

tracker = TaskTracker()
tracker.add("Walk dog")
tracker.add("Put bins out")
tracker.add("Wash car")
assert tracker.list_incomplete() == ["Walk dog", "Put bins out", "Wash car"]

tracker = TaskTracker()
tracker.add("Walk dog")
tracker.add("Put bins out")
tracker.add("Wash car")
tracker.mark_complete(2)
assert tracker.list_incomplete() == ["Walk dog", "Put bins out"]

tracker = TaskTracker()
tracker.add("Wash car")
tracker.mark_complete(-1) raise error "Task doesn't exist"

tracker = TaskTracker()
tracker.add("Wash car")
tracker.mark_complete(2) raise error "Task doesn't exist"
------------