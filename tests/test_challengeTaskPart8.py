from lib.challengeTaskPart8 import *
import pytest

def test_todo_initialization():
    todo = Todo("Do the laundry")
    assert todo.task == "Do the laundry"
    assert not todo.complete

def test_mark_complete():
    todo = Todo("Go grocery shopping")
    todo.mark_complete()
    assert todo.complete

def test_todo_list_add():
    todo_list = TodoList()
    todo = Todo("Read a book")
    todo_list.add(todo)
    assert todo_list.todos == [todo]

def test_incomplete_todos():
    todo_list = TodoList()
    todo1 = Todo("Write code")
    todo2 = Todo("Exercise")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo2.mark_complete()
    assert todo_list.incomplete() == [todo1]

def test_complete_todos():
    todo_list = TodoList()
    todo1 = Todo("Write code")
    todo2 = Todo("Exercise")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo2.mark_complete()
    assert todo_list.complete() == [todo2]

def test_give_up():
    todo_list = TodoList()
    todo1 = Todo("Write code")
    todo2 = Todo("Exercise")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.give_up()
    assert all(todo.complete for todo in todo_list.todos)