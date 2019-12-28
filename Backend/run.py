import os
from app import app
# from apscheduler.schedulers.background import BackgroundScheduler

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='37.148.209.203', port=port, debug=False, use_reloader=False)
    # scheduler = BackgroundScheduler()
    # scheduler.add_job(func=checkWaiting, trigger="interval" , seconds=60)
    # scheduler.start()