import time
from linenotify import send_line_notify

def run():
    return send_line_notify("これはテストです")

while True:
    run()
    time.sleep(100)
