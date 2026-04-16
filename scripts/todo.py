#!/usr/bin/env python3
"""Persistent todo list manager. Stores tasks in a local JSON file."""

import sys
import json
import os

TODO_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "todos.json")


def load_todos() -> list[dict]:
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return json.load(f)


def save_todos(todos: list[dict]):
    os.makedirs(os.path.dirname(TODO_FILE), exist_ok=True)
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=2)


def get_remaining(todos: list[dict]) -> list[dict]:
    """Return pending tasks for auto-listing after actions."""
    remaining = []
    for i, t in enumerate(todos, 1):
        if not t["done"]:
            remaining.append({"number": i, "description": t["description"]})
    return remaining


def add_task(description: str) -> dict:
    todos = load_todos()
    task = {"description": description, "done": False}
    todos.append(task)
    save_todos(todos)
    return {"action": "added", "task": description, "number": len(todos),
            "remaining": get_remaining(todos)}


def list_tasks() -> dict:
    todos = load_todos()
    if not todos:
        return {"action": "list", "tasks": [], "message": "Todo list is empty."}
    tasks = []
    for i, t in enumerate(todos, 1):
        status = "done" if t["done"] else "pending"
        tasks.append({"number": i, "description": t["description"], "status": status})
    return {"action": "list", "tasks": tasks, "total": len(todos)}


def mark_done(number: int) -> dict:
    todos = load_todos()
    if number < 1 or number > len(todos):
        return {"error": f"Invalid task number {number}. You have {len(todos)} tasks."}
    todos[number - 1]["done"] = True
    save_todos(todos)
    return {"action": "done", "task": todos[number - 1]["description"], "number": number,
            "remaining": get_remaining(todos)}


def remove_task(number: int) -> dict:
    todos = load_todos()
    if number < 1 or number > len(todos):
        return {"error": f"Invalid task number {number}. You have {len(todos)} tasks."}
    removed = todos.pop(number - 1)
    save_todos(todos)
    return {"action": "removed", "task": removed["description"],
            "remaining": get_remaining(todos)}


def clear_completed() -> dict:
    todos = load_todos()
    original_count = len(todos)
    todos = [t for t in todos if not t["done"]]
    cleared = original_count - len(todos)
    save_todos(todos)
    return {"action": "cleared", "cleared_count": cleared,
            "remaining": get_remaining(todos)}


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: todo.py <add|list|done|remove|clear> [args]"}))
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "add":
        if len(sys.argv) < 3:
            result = {"error": "Please provide a task description."}
        else:
            description = " ".join(sys.argv[2:])
            result = add_task(description)
    elif command == "list":
        result = list_tasks()
    elif command == "done":
        if len(sys.argv) < 3:
            result = {"error": "Please provide a task number."}
        else:
            result = mark_done(int(sys.argv[2]))
    elif command == "remove":
        if len(sys.argv) < 3:
            result = {"error": "Please provide a task number."}
        else:
            result = remove_task(int(sys.argv[2]))
    elif command == "clear":
        result = clear_completed()
    else:
        result = {"error": f"Unknown command '{command}'. Use: add, list, done, remove, clear"}

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
