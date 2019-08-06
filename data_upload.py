from datetime import date, timedelta

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

date_today = date.today()
date_today_str = str(date_today.month) + '/' + str(date_today.day) + '/' + str(date_today.year)

def upload_file():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    print("successful auth")
    drive = GoogleDrive(gauth)
    data = drive.CreateFile(metadata={"title": date_today_str + "_finances.csv"})
    print("file created")
    data.SetContentFile('./out.csv')
    print("file content set")
    data.Upload()
    print("file uploaded, goodbye")

    data = drive.CreateFile(metadata={"title": date_today_str + "common_merchants.png"})
    print("file created")
    data.SetContentFile('./common_merchants.png')
    print("file content set")
    data.Upload()
    print("file uploaded, goodbye")

    data = drive.CreateFile(metadata={"title": date_today_str + "per_day.png"})
    print("file created")
    data.SetContentFile('./out.csv')
    print("file content set")
    data.Upload()
    print("file uploaded, goodbye")
