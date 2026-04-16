# Todo Manager — Forex Bot Improvement Tracker

## Description
Track and manage improvement tasks for the Forex RL Trading Bot capstone project. This is a smart todo list that understands the forex bot's architecture and can suggest relevant improvements when asked.

## Trigger
When the user asks about:
- Adding a task or improvement (e.g., "add Streamlit dashboard to my list")
- Viewing tasks (e.g., "show my todos", "what's left to do on the forex bot")
- Completing or checking off tasks (e.g., "mark task 1 as done")
- Removing or clearing tasks (e.g., "remove task 2", "clear completed tasks")
- What to work on next for the forex bot (e.g., "what should I improve next?")
- Any mention of "todo", "task list", "to-do", "improvements", or "what's left"

## Forex Bot Context
The forex bot is a DQN reinforcement learning trading bot located at `~/Desktop/Capstone/forex-bot/`. Key architecture:
- **Environment:** `src/environment/forex_env.py` (basic) and `feature_env.py` (with technical indicators)
- **Agent:** `src/agents/dqn_agent.py` (Stable-Baselines3 DQN)
- **Baselines:** `src/agents/baselines.py` (Buy-and-Hold, SMA Crossover, Random)
- **Evaluation:** `src/backtesting/evaluate.py` (Sharpe, Max Drawdown, Win Rate, Profit Factor)
- **Features:** `src/features/indicators.py` (RSI, MACD, BB, ATR, SMA)
- **Data:** yfinance + FRED fetch scripts, 5 currency pairs
- **Demo:** `demo.py` — end-to-end pipeline
- **Pre-trained models:** `models/dqn_EURUSD.zip`, `models/dqn_feature_EURUSD.zip`

## Instructions

1. Determine which operation the user wants:
   - **add** — Adding a new improvement task
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
   > 📋 Remaining improvements:
   > 1. Task one
   > 2. Task three

   **Listing tasks:**
   > 📋 Forex Bot Improvement Tracker:
   > 1. [ ] Task one
   > 2. [x] Task two (completed)
   > 3. [ ] Task three

   **After completing:**
   > ✅ Marked as done: "<task>"
   >
   > 📋 Remaining improvements:
   > (list from `remaining` field)

   **After removing:**
   > 🗑️ Removed: "<task>"
   >
   > 📋 Remaining improvements:
   > (list from `remaining` field)

   **After clearing:**
   > 🧹 Cleared <N> completed tasks.
   >
   > 📋 Remaining improvements:
   > (list from `remaining` field)

   If `remaining` is an empty list after any action, say:
   > 🎉 All improvements done! The forex bot is in great shape.

5. **When asked "what should I work on next?"** — Run `python3 scripts/todo.py list`, look at the pending tasks, and recommend the highest-priority one based on:
   - Impact on the demo/grading (Streamlit dashboard = high impact)
   - Dependencies (some tasks need others done first)
   - Difficulty (suggest easier wins if many tasks remain)

6. If the list is empty when listing, say:
   > 📋 No improvements tracked yet. Add one with "add <task> to my list".
   > Suggestion: Start with the Streamlit dashboard or walk-forward validation.

## Edge Cases
- If user says "done 99" but only 3 tasks exist, inform them the task number is invalid
- If user says "add" with no description, ask what they'd like to add
- Tasks persist between conversations (stored in data/todos.json)
