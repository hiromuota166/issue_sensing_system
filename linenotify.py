# LINEに通知を送る関数
from dotenv import load_dotenv
import os
import requests
load_dotenv()

# APIのURLとトークン
url = "https://notify-api.line.me/api/notify"

access_token = [os.environ.get("LINE_NOTIFY")]

message = "こーとがあいてるよ！"

def send_line_notify(message):
  for token in access_token:
    headers = {"Authorization" : "Bearer "+ token}
    send_data = {"message" :  message}
    result = requests.post(url, headers = headers, data = send_data)
    print(result)

if __name__ == "__main__":
  send_line_notify("デフォルト")