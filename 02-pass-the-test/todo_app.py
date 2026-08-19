"""A Todo List application.

Runs WITHOUT any user input - a hard-coded workflow in main() demonstrates
the TodoApp class.

BUGS: This file intentionally contains bugs. Find them and fix them so that
all 36 tests in test_todo_app.py pass.
"""


class TodoApp:
    """A minimal todo list stored as a list of {"task", "done"} dicts."""

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a task. Returns True on success.

        A task is rejected (returns False) when it is empty/whitespace-only
        or a duplicate of an existing task (compared case-insensitively).
        """
        if not task or not task.strip():
            return False
        if any(existing["task"].lower() == task.lower() for existing in self.tasks):
            return False
        self.tasks.append({"task": task, "done": False})
        return True

    def remove_task(self, task):
        """Remove a task (matched case-insensitively). Returns True if removed."""
        for item in self.tasks:
            if item["task"].lower() == task.lower():
                self.tasks.remove(item)
                return True
        return False

    def mark_complete(self, task):
        """Mark a task done. Returns True only if the task exists."""
        for item in self.tasks:
            if item["task"].lower() == task.lower():
                item["done"] = True
                return True
        return False

    def mark_incomplete(self, task):
        """Mark a task not-done. Returns True only if the task exists."""
        for item in self.tasks:
            if item["task"] == task:
                item["done"] = False
                return True
        return False

    def pending_tasks(self):
        """Return the NAMES of the not-done tasks, in insertion order."""
        return [item["task"] for item in self.tasks if not item["done"]]

    def completed_tasks(self):
        """Return the NAMES of the done tasks, in insertion order."""
        return [item["task"] for item in self.tasks if item["done"]]

    def all_tasks(self):
        """Return all task names, in insertion order."""
        return [item["task"] for item in self.tasks]

    def task_count(self):
        """Total number of tasks."""
        return len(self.tasks)

    def pending_count(self):
        """Number of not-done tasks."""
        return len(self.pending_tasks())

    def completed_count(self):
        """Number of done tasks."""
        return len(self.completed_tasks())

    def search(self, keyword):
        """Return task names containing keyword (case-insensitive)."""
        return [item["task"] for item in self.tasks if keyword.lower() in item["task"].lower()]

    def clear_completed(self):
        """Remove all done tasks."""
        self.tasks = [item for item in self.tasks if not item["done"]]

    def clear_all(self):
        """Remove every task."""
        self.tasks.clear()

    def is_empty(self):
        """True when there are no tasks at all."""
        return len(self.tasks) == 0

    def get_task(self, index):
        """Return the task name at index, or None when out of range."""
        if index < 0 or index >= len(self.tasks):
            return None
        return self.tasks[index]["task"]


def main():
    app = TodoApp()
    app.add_task("Buy groceries")
    app.add_task("Walk the dog")
    app.add_task("Write code")
    app.mark_complete("Buy groceries")
    print("Pending:", app.pending_tasks())
    print("Completed:", app.completed_tasks())


if __name__ == "__main__":
    main()