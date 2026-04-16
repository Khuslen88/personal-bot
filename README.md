# Personal Telegram Bot (Claude Channels)

A personal assistant bot powered by Claude Code and connected via Telegram using Claude Channels. The bot provides six custom skills covering forex trading, news research, task management, weather, charting, and translation.

## Skills

| Skill | Description | Example |
|-------|-------------|---------|
| Forex Rate | Look up live exchange rates for any currency pair | "What's the EUR/USD rate?" |
| Forex Chart | Generate ASCII price charts for currency pairs | "Show me the USD/EUR chart for the last month" |
| News Researcher | Search and summarize recent news on any topic | "What's the latest news about AI?" |
| Todo Manager | Manage a persistent todo list | "Add 'finish homework' to my todo list" |
| Weather | Get current weather for any city worldwide | "Weather in Ulaanbaatar" |
| Translation | Translate text between 15+ languages | "Translate 'hello' to Mongolian" |

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
- "Weather in Tokyo"
- "Translate 'thank you' to Korean"

## Skill Details

### Forex Rate Lookup
Fetches real-time exchange rates using the open.er-api.com public API. Supports all major currency pairs (USD, EUR, GBP, JPY, MNT, etc.) with optional amount conversion.

**Example interactions:**
- "What's the EUR/USD exchange rate?"
- "Convert 100 USD to MNT"
- "Show me the rate for GBP to EUR"

### Forex Chart
Generates ASCII price charts for any currency pair using historical data from Yahoo Finance. Supports configurable time periods (1 week to 1 year) with summary statistics.

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

### Todo Manager
Manages a persistent todo list stored locally in JSON. Supports adding, listing, completing, and removing tasks. Data persists between conversations.

**Example interactions:**
- "Add 'study for exam' to my todo list"
- "Show my todo list"
- "Mark task 1 as done"
- "Remove completed tasks"

### Weather Lookup
Gets current weather conditions for any city worldwide using wttr.in (no API key needed). Includes temperature, humidity, wind speed, and feels-like temperature.

**Example interactions:**
- "Weather in Ulaanbaatar"
- "Is it cold in New York?"
- "What's the weather like in Tokyo?"

### Translation
Translates text between 15+ languages using the MyMemory free API. Supports auto-detection of source language and includes Mongolian language support.

**Example interactions:**
- "Translate 'hello' to Japanese"
- "How do you say 'goodbye' in Mongolian?"
- "What does 'сайн байна уу' mean?"

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
│       ├── todo-manager/
│       │   └── SKILL.md
│       ├── weather/
│       │   └── SKILL.md
│       └── translation/
│           └── SKILL.md
├── scripts/
│   ├── fetch_rate.py
│   ├── forex_chart.py
│   ├── todo.py
│   └── translate.py
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
- `feature/weather-skill` — Weather lookup skill
- `feature/translation-skill` — Translation skill

Each skill had a corresponding GitHub issue for tracking (#1–#6).

Worktrees were used to develop multiple skills simultaneously without branch switching:
```bash
git worktree add ../personal-bot-news feature/news-skill
git worktree add ../personal-bot-todo feature/todo-skill
git worktree add ../personal-bot-chart feature/forex-chart-skill
git worktree add ../personal-bot-weather feature/weather-skill
git worktree add ../personal-bot-translate feature/translation-skill
```

## Author

Khuslen Batnasan — Data Science, Spring 2026
