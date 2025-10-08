# BetFetcher (Render-ready)

This project is prepared to deploy a Telegram-based betting signal fetcher on Render.com.
It includes a simple fetcher loop, notifier, and placeholders for parsing & analysis logic.

## Quick start (local test)
1. Copy `.env.example` -> `.env` and fill your values (BOT_TOKEN, ADMIN_ID).
2. Create virtual environment and install dependencies:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Run a local test message:
```
python bot_test.py
```
You should receive a test message in Telegram from your bot.

## Deploy to Render (worker)
1. Push this repository to GitHub.
2. Create a new **Worker** service on Render, connect repo.
3. Set Start Command: `python main.py`
4. Add environment variables in Render dashboard: BOT_TOKEN, ADMIN_ID, UPDATE_INTERVAL, API_URL (if available).
5. Deploy — Render will install dependencies and run the bot.

## Notes
- This template assumes external API for odds (API_URL). If you want to scrape pari.ru directly, implement parsing logic in `fetcher.py` and `parser.py`.
- Be careful with scraping: follow site's Terms of Service.
