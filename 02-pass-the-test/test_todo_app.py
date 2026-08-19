"""36 pytest tests describing the expected (correct) behaviour of TodoApp.

These tests encode the specification. They are written against the FIXED
behaviour, so several currently fail against the buggy todo_app.py - fix the
bugs in todo_app.py until every test here passes.
"""

import pytest

from todo_app import TodoApp


def _app_with(*tasks):
    app = TodoApp()
    for task in tasks:
        app.add_task(task)
    return app


# --- add_task ---------------------------------------------------------------

def test_add_task_returns_true_for_valid_task():
    assert TodoApp().add_task("Buy milk") is True


def test_add_task_appends_task():
    app = _app_with("Buy milk")
    assert app.all_tasks() == ["Buy milk"]


def test_add_task_rejects_exact_duplicate():
    app = _app_with("Buy milk")
    assert app.add_task("Buy milk") is False


def test_add_task_rejects_empty_string():
    assert TodoApp().add_task("") is False


def test_add_task_rejects_whitespace_only():
    assert TodoApp().add_task("   ") is False


def test_add_task_rejects_duplicate_ignoring_case():
    app = _app_with("Walk the dog")
    assert app.add_task("walk the dog") is False


# --- remove_task ------------------------------------------------------------

def test_remove_task_returns_true_for_existing():
    app = _app_with("Buy milk")
    assert app.remove_task("Buy milk") is True


def test_remove_task_removes_task():
    app = _app_with("Buy milk", "Write code")
    app.remove_task("Buy milk")
    assert app.all_tasks() == ["Write code"]


def test_remove_task_matches_ignoring_case():
    app = _app_with("Walk the dog")
    assert app.remove_task("WALK THE DOG") is True


def test_remove_task_missing_returns_false():
    app = _app_with("Buy milk")
    assert app.remove_task("Nope") is False


def test_remove_task_removes_only_one_occurrence():
    app = TodoApp()
    app.tasks = [
        {"task": "A", "done": False},
        {"task": "A", "done": False},
        {"task": "B", "done": False},
    ]
    app.remove_task("A")
    assert app.all_tasks() == ["A", "B"]


# --- mark_complete / mark_incomplete ---------------------------------------

def test_mark_complete_returns_true_for_existing():
    app = _app_with("Buy milk")
    assert app.mark_complete("Buy milk") is True


def test_mark_complete_marks_done():
    app = _app_with("Buy milk")
    app.mark_complete("Buy milk")
    assert app.completed_count() == 1
    assert app.pending_count() == 0


def test_mark_complete_missing_returns_false():
    app = _app_with("Buy milk")
    assert app.mark_complete("Nope") is False


def test_mark_complete_twice_is_idempotent():
    app = _app_with("Buy milk")
    app.mark_complete("Buy milk")
    app.mark_complete("Buy milk")
    assert app.completed_count() == 1


def test_mark_incomplete_returns_true_for_done_task():
    app = _app_with("Buy milk")
    app.mark_complete("Buy milk")
    assert app.mark_incomplete("Buy milk") is True


def test_mark_incomplete_marks_not_done():
    app = _app_with("Buy milk")
    app.mark_complete("Buy milk")
    app.mark_incomplete("Buy milk")
    assert app.pending_count() == 1
    assert app.completed_count() == 0


def test_mark_incomplete_missing_returns_false():
    assert TodoApp().mark_incomplete("Nope") is False


# --- pending_tasks / completed_tasks ----------------------------------------

def test_pending_tasks_only_pending():
    app = _app_with("Buy milk", "Write code")
    app.mark_complete("Buy milk")
    assert app.pending_tasks() == ["Write code"]


def test_pending_tasks_keeps_insertion_order():
    app = _app_with("a", "b", "c")
    app.mark_complete("b")
    assert app.pending_tasks() == ["a", "c"]


def test_completed_tasks_only_completed():
    app = _app_with("Buy milk", "Write code")
    app.mark_complete("Buy milk")
    assert app.completed_tasks() == ["Buy milk"]


def test_completed_tasks_keeps_insertion_order():
    app = _app_with("a", "b", "c")
    app.mark_complete("b")
    app.mark_complete("c")
    assert app.completed_tasks() == ["b", "c"]


# --- counts -----------------------------------------------------------------

def test_task_count_empty():
    assert TodoApp().task_count() == 0


def test_task_count_after_adds():
    assert _app_with("a", "b", "c").task_count() == 3


def test_pending_count():
    app = _app_with("a", "b")
    app.mark_complete("a")
    assert app.pending_count() == 1


def test_completed_count():
    app = _app_with("a", "b")
    app.mark_complete("a")
    assert app.completed_count() == 1


# --- search -----------------------------------------------------------------

def test_search_finds_substring():
    app = _app_with("Buy milk", "Walk the dog")
    assert app.search("milk") == ["Buy milk"]


def test_search_is_case_insensitive():
    app = _app_with("Walk the dog")
    assert app.search("WALK") == ["Walk the dog"]


def test_search_no_match_returns_empty_list():
    app = _app_with("Buy milk")
    assert app.search("xyz") == []


# --- clear_completed ---------------------------------------------------------

def test_clear_completed_removes_only_done():
    app = _app_with("a", "b")
    app.mark_complete("a")
    app.clear_completed()
    assert app.all_tasks() == ["b"]


def test_clear_completed_keeps_pending():
    app = _app_with("a", "b", "c")
    app.mark_complete("a")
    app.clear_completed()
    assert app.pending_tasks() == ["b", "c"]


# --- is_empty / get_task -----------------------------------------------------

def test_is_empty_true_initial():
    assert TodoApp().is_empty() is True


def test_is_empty_false_after_add():
    assert _app_with("a").is_empty() is False


def test_get_task_valid_index():
    app = _app_with("a", "b")
    assert app.get_task(1) == "b"


def test_get_task_out_of_range_returns_none():
    assert _app_with("a").get_task(5) is None


def test_all_tasks_returns_insertion_order():
    assert _app_with("x", "y", "z").all_tasks() == ["x", "y", "z"]