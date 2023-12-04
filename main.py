from linenotify import send_line_notify

def run():
    return send_line_notify("cron job")

if __name__ == "__main__":
    run()