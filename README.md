# Personal Telegram Bot (Claude Channels)

A personal assistant bot powered by Claude Code and connected via Telegram using Claude Channels. The bot provides four custom skills covering forex trading, news research, task management, and charting.

## Skills

| Skill | Description | Example |
|-------|-------------|---------|
| Forex Rate | Look up live exchange rates for any currency pair | "What's the EUR/USD rate?" |
| Forex Chart | Generate ASCII price charts for currency pairs | "Show me the USD/EUR chart for the last month" |
| News Researcher | Search and summarize recent news on any topic | "What's the latest news about AI?" |
| Todo Manager | Forex bot improvement tracker — tracks and prioritizes capstone tasks | "What should I work on next?" |

## Setup Instructions

### Prerequisites
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed
- Python 3 with `yfinance` package (`pip install yfinance`)
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
- "Show me the EUR/USD chart"
- "Find me news about climate change"
- "Add buy groceries to my todo list"

## Skill Details

### Forex Rate Lookup
Fetches real-time exchange rates using the open.er-api.com public API. Supports all major currency pairs (USD, EUR, GBP, JPY, MNT, etc.) with optional amount conversion.

**Example interactions:**
- "What's the EUR/USD exchange rate?"
- "Convert 100 USD to MNT"
- "Show me the rate for GBP to EUR"

### Forex Chart
Generates ASCII price charts for any currency pair using historical data from Yahoo Finance. Supports configurable time periods (1 week to 1 year) with summary statistics including open, close, high, low, and change percentage.

**Example interactions:**
- "Chart for EUR/USD last 30 days"
- "How has the dollar moved this month?"
- "USD/JPY trend over 3 months"

### News Researcher
Searches the web for recent news on any topic and provides a concise summary with key points and source attribution.

**Example interactions:**
- "What's happening with Bitcoin today?"
- "Latest news about Mongolia"
- "Summarize recent AI developments"

### Todo Manager (Forex Bot Improvement Tracker)
A smart todo list connected to the Forex RL Trading Bot capstone project. It comes pre-loaded with improvement tasks (Streamlit dashboard, walk-forward validation, trade journal, etc.) and understands the bot's architecture. After every action, it auto-shows remaining tasks. Can also recommend what to work on next based on priority and impact.

**Example interactions:**
- "What should I work on next?" → recommends highest-impact task
- "Show my todo list" → lists all improvements with status
- "Mark task 1 as done" → shows remaining improvements
- "Add 'optimize reward function' to my list"

## Project Structure
```
personal-bot/
├── .claude/
│   └── skills/
│       ├── forex-rate/
│       │   └── SKILL.md
│       ├── forex-chart/
│       │   └── SKILL.md
│       ├── news-researcher/
│       │   └── SKILL.md
│       └── todo-manager/
│           └── SKILL.md
├── scripts/
│   ├── fetch_rate.py
│   ├── forex_chart.py
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
- `feature/forex-chart-skill` — Forex chart visualization skill

Each skill had a corresponding GitHub issue for tracking.

Worktrees were used to develop multiple skills simultaneously without branch switching:
```bash
git worktree add ../personal-bot-news feature/news-skill
git worktree add ../personal-bot-todo feature/todo-skill
git worktree add ../personal-bot-chart feature/forex-chart-skill
```

## Author

Khuslen Batnasan — Data Science, Spring 2026
