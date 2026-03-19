from flask import Flask, request, redirect
from datetime import datetime, timedelta

app = Flask(__name__)

# database sederhana (max 100 user)
users = {
    "USER001": {"created": datetime(2026, 3, 19), "expired_days": 7, "download_count": 0},
    "USER002": {"created": datetime(2026, 3, 19), "expired_days": 7, "download_count": 0},
    "USER003": {"created": datetime(2026, 3, 19), "expired_days": 7, "download_count": 0},
    # lanjutkan sampai USER100
}

MAX_DOWNLOAD = 3

GDRIVE_LINK = "https://drive.google.com/file/d/ISI_LINK_FILE_KAMU/view"

@app.route('/')
def home():
    return "5MakerD'sign Server Aktif"

@app.route('/download')
def download():
    key = request.args.get('key')

    if key not in users:
        return "Key tidak valid"

    user = users[key]

    # cek expired
    expire_time = user["created"] + timedelta(days=user["expired_days"])
    if datetime.now() > expire_time:
        return "Link expired"

    # cek limit download
    if user["download_count"] >= MAX_DOWNLOAD:
        return "Limit download tercapai"

    # tambah count
    user["download_count"] += 1

    return redirect(GDRIVE_LINK)

app.run(host='0.0.0.0', port=3000)
