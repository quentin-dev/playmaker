import json
import os
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

from telegram.ext import Updater

def handler(event, context):

    token = os.environ["TELEGRAM_TOKEN"]
    chat_id = int(os.environ["TELEGRAM_CHAT_ID"])

    urls = json.loads(os.environ["URLS"])

    contents = "STATUS REPORT\n\n"

    alert = False
    
    for url in urls:
        request = Request(url)
        try:
            urlopen(request)
            contents += f"{url} is OK\n"
        except URLError as u:
            alert = True
            contents += f"{url} is NOT OK - Reason: {u.reason}\n"
        except HTTPError as e:
            alert = True
            contents += f"{url} is NOT OK - Code: {e.code()}\n"

    if alert:
        updater = Updater(token=token)
        updater.bot.send_message(chat_id=chat_id, text=contents)
        updater.stop()

    return {
        "statusCode": 200,
        "body": json.dumps(contents)
    }

if __name__ == "__main__":
    handler(event=None, context=None)