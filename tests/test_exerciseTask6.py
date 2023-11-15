import pytest
from lib.exerciseTask6 import *

def test_tracker_has_no_tasks():
    tracker = TaskTracker()
    assert tracker.list_incomplete() == []

def test_returns_list_with_tasks():
    tracker = TaskTracker()
    tracker.add("Walk dog")
    assert tracker.list_incomplete() == ["Walk dog"]

def test_returns_list_with_multiple_tasks():
    tracker = TaskTracker()
    tracker.add("Walk dog")
    tracker.add("Put bins out")
    tracker.add("Wash car")
    assert tracker.list_incomplete() == ["Walk dog", "Put bins out", "Wash car"]

def test_mark_complete_removes_index_of_task():
    tracker = TaskTracker()
    tracker.add("Walk dog")
    tracker.add("Put bins out")
    tracker.add("Wash car")
    tracker.mark_complete(2)
    assert tracker.list_incomplete() == ["Walk dog", "Put bins out"]
 
def test_mark_incomplete_doesnt_remove_anything_when_index_out_range():
    tracker = TaskTracker()
    tracker.add("Wash car")
    with pytest.raises(Exception) as e:
        tracker.mark_complete(-1)
    assert str(e.value) == "Task doesn't exist"
    assert tracker.list_incomplete() == ["Wash car"]

    with pytest.raises(Exception) as e: 
        tracker.mark_complete(2)
    assert str(e.value) == "Task doesn't exist"
    assert tracker.list_incomplete() == ["Wash car"]