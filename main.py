import time
from linenotify import send_line_notify
import schedule

def run():
    return send_line_notify("これはテストです")

# 火曜日の午前1時に実行
schedule.every().tuesday.at("01:00").do(run)

if __name__ == "__main__":
    schedule.run_pending()
    time.sleep(100)