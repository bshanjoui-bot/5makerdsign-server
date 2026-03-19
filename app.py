from flask import Flask, request, redirect
from datetime import datetime, timedelta

app = Flask(__name__)

# database sederhana
users = {
    "USER123": {
        "created": datetime(2026, 3, 19),
        "expired_days": 7
    }
}

# link folder GDrive kamu
GDRIVE_LINK = "https://drive.google.com/drive/folders/1lVfYDM620WOhTWjJFAKLc5ZT17cAV2gg"

@app.route('/')
def home():
    return "5MakerD'sign Server Aktif"

@app.route('/download')
def download():
    key = request.args.get('key')

    if key not in users:
        return "Key tidak valid"

    user = users[key]
    expire_time = user["created"] + timedelta(days=user["expired_days"])

    if datetime.now() > expire_time:
        return "Link expired"

    return redirect(GDRIVE_LINK)

app.run(host='0.0.0.0', port=3000)
