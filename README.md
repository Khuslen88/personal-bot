# Personal Telegram Bot (Claude Channels)

A personal assistant bot powered by Claude Code and connected via Telegram using Claude Channels. The bot provides three custom skills: live forex exchange rates, news research and summarization, and a persistent todo list manager.

## Skills

| Skill | Description | Example |
|-------|-------------|---------|
| Forex Rate | Look up live exchange rates for any currency pair | "What's the EUR/USD rate?" |
| News Researcher | Search and summarize recent news on any topic | "What's the latest news about AI?" |
| Todo Manager | Manage a persistent todo list | "Add 'finish homework' to my todo list" |

## Setup Instructions

### Prerequisites
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed
- A Telegram account
- A Telegram bot token (from [@BotFather](https://t.me/botfather))

### 1. Create Telegram Bot
1. Open Telegram and message [@BotFather](https://t.me/botfather)
2. Send `/newbot` and follow the prompts
3. Save the bot token you receive

### 2. Configure Claude Channels
```bash
# Navigate to the project directory
cd personal-bot/

# Start Claude Code with Telegram channel
claude --channel telegram
```

Follow the prompts to enter your bot token. Claude Code will connect to Telegram and start listening for messages.

### 3. Test the Bot
Send a message to your bot on Telegram. Try:
- "What's the exchange rate for USD to JPY?"
- "Find me news about climate change"
- "Add buy groceries to my todo list"

## Skill Details

### Forex Rate Lookup
Fetches real-time exchange rates using a public API. Supports all major currency pairs (USD, EUR, GBP, JPY, etc.).

**Example interactions:**
- "What's the EUR/USD exchange rate?"
- "Convert 100 USD to MNT"
- "Show me the rate for GBP to EUR"

### News Researcher
Searches the web for recent news on any topic and provides a concise summary with key points.

**Example interactions:**
- "What's happening with Bitcoin today?"
- "Latest news about Mongolia"
- "Summarize recent AI developments"

### Todo Manager
Manages a persistent todo list stored locally. Supports adding, listing, completing, and removing tasks.

**Example interactions:**
- "Add 'study for exam' to my todo list"
- "Show my todo list"
- "Mark task 1 as done"
- "Remove completed tasks"

## Project Structure
```
personal-bot/
├── .claude/
│   └── skills/
│       ├── forex-rate/
│       │   └── SKILL.md
│       ├── news-researcher/
│       │   └── SKILL.md
│       └── todo-manager/
│           └── SKILL.md
├── scripts/
│   ├── fetch_rate.py
│   └── todo.py
├── data/
│   └── todos.json
├── README.md
└── .gitignore
```

## Git Workflow

This project was developed using feature branches and git worktrees for parallel development:

- `feature/forex-skill` — Forex rate lookup skill
- `feature/news-skill` — News researcher skill  
- `feature/todo-skill` — Todo manager skill

Each skill had a corresponding GitHub issue for tracking.

## Author

Khuslen Batnasan — Data Science, Spring 2026
