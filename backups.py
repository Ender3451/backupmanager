import shutil
import datetime
from datetime import date
import os.path
import time
today = date.today()

src = f'C:\\Users\\Ender\\Documents\\AAminecraft\\latest.mcworld'
dst = f'D:\\mcbackups\\{today}backup.mcworld'
if os.path.exists(src):
    shutil.move(src, dst)
    print("Backup created successfully.")
