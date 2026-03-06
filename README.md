# latex_formula_bot

A minimalist Discord bot built with discord.py and matplotlib that renders LaTeX mathematical equations into images.

## Local Installation

```bash
git clone https://github.com/Thomas-Chambon/latex_formula_bot.git
cd latex_formula_bot
```
### Without Docker

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```
2. **Configure environment:**

Create a `.env` file in the root directory:
```env
DISCORD_TOKEN=your_bot_token_here
```
3. **Run the bot:**
```bash
python main.py
```
--- 

### With Docker

1. **Configure environment:**

Create a `.env` file in the root directory:
```env
DISCORD_TOKEN=your_bot_token_here
```

2. **Run the bot:**
```bash 
docker compose up --build 
```
---

## Discord Setup

To integrate the bot into your Discord environment:

1. **Create an Application**: Go to the [Discord Developer Portal](https://discord.com/developers/applications).


2. **Bot Permissions**:
* Enable **Message Content Intent** in the "Bot" tab.
* Ensure the bot has `Send Messages` and `Attach Files` permissions.

3. **OAuth2 URL Generator**:
* Select the `bot` and `applications.commands` scopes.
* Under bot permissions, select `Read Messages/View Channels`, `Send Messages`, and `Attach Files`.

4. Copy the generated URL into your browser to add the bot to your server.

---
## Usage
* `/tex [equation]` — Renders math (e.g., `/tex \sum_{i=1}^{n} i`)
* `/help` — Displays usage instructions
---

## Author 
[Thomas Chambon](https://github.com/Thomas-Chambon/)
