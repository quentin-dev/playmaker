# Playmaker

A simple telegram bot to monitor my self-hosted services

## Getting Started

### Environment variables

- `TELEGRAM_TOKEN`: Your Telegram bot token
- `TELEGRAM_CHAT_ID`: The ID of the conversation you want to send the alerts to
- `URLS`: A JSON array of the urls you want to ping

### Running the bot

```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements
python playmaker.py
```

### Using the packaging script

If you want to run the bot on AWS Lambda you can use the given `create-package.sh` script to create the zip file you can upload directly. Be sure to activate your venv before running the scripts.


![Playmaker on his board](https://static.zerochan.net/Playmaker.full.2097075.jpg)