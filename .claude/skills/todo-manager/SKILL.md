# Todo Manager

## Description
Manage a persistent todo list stored locally. Supports adding, listing, completing, and removing tasks.

## Trigger
When the user asks about:
- Adding a task or reminder (e.g., "add buy groceries to my todo list")
- Viewing their tasks (e.g., "show my todos", "what's on my list")
- Completing or checking off tasks (e.g., "mark task 1 as done")
- Removing or clearing tasks (e.g., "remove task 2", "clear completed tasks")
- Any mention of "todo", "task list", "to-do", or "checklist"

## Instructions

1. Determine which operation the user wants:
   - **add** — Adding a new task
   - **list** — Viewing all tasks
   - **done** — Marking a task as complete
   - **remove** — Removing a specific task
   - **clear** — Removing all completed tasks

2. Run the appropriate command:
   ```bash
   python3 scripts/todo.py add "<task description>"
   python3 scripts/todo.py list
   python3 scripts/todo.py done <task_number>
   python3 scripts/todo.py remove <task_number>
   python3 scripts/todo.py clear
   ```

3. The script returns JSON with a `remaining` field listing all pending tasks. **Always show remaining tasks** after any action so the user knows what's left to do.

4. Format the response based on the operation:

   **After adding:**
   > ✅ Added: "<task>" (Task #<number>)
   >
   > 📋 Remaining tasks:
   > 1. Task one
   > 2. Task three

   **Listing tasks:**
   > 📋 Your Todo List:
   > 1. [ ] Task one
   > 2. [x] Task two (completed)
   > 3. [ ] Task three

   **After completing:**
   > ✅ Marked as done: "<task>"
   >
   > 📋 Remaining tasks:
   > 1. Task one
   > 3. Task three

   **After removing:**
   > 🗑️ Removed: "<task>"
   >
   > 📋 Remaining tasks:
   > (list from `remaining` field)

   **After clearing:**
   > 🧹 Cleared <N> completed tasks.
   >
   > 📋 Remaining tasks:
   > (list from `remaining` field)

   If `remaining` is an empty list after any action, say:
   > 🎉 All done! No remaining tasks.

5. If the list is empty when listing, say:
   > 📋 Your todo list is empty. Add a task by saying "add <task> to my todo list".

## Edge Cases
- If user says "done 99" but only 3 tasks exist, inform them the task number is invalid
- If user says "add" with no description, ask what they'd like to add
- Tasks persist between conversations (stored in data/todos.json)
