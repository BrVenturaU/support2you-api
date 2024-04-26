import os
import shutil

def ensure_db_exists():
    exists = os.path.exists("./data/Support2YouDb.db")
    if(not exists):
        shutil.copy("./defaults/Support2YouDb.db", "./data/Support2YouDb.db")