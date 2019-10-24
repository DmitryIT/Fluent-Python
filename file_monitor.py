import argparse
import os
from datetime import datetime, timedelta
from time import sleep

"""
Monitor an input file and throw a message if it
is older then MAX_DELTA
Syntax: python file_monitor.py <path to file> 
"""

MAX_DELTA = timedelta(minutes=1)


def file_monitor():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="absolute path to file")
    args = parser.parse_args()

    fd = args.file
    # fd = os.path.join(PATH, NAME)

    if os.path.exists(fd):
        while True:
            statinfo = os.stat(fd)

            now = datetime.now()
            mtime = datetime.fromtimestamp(statinfo.st_mtime)
            delta = now - mtime

            if delta > MAX_DELTA:
                print(fd + " is outdated")
                print("mtime = " + str(mtime))
                print("now =   " + str(now))
                break

            sleep(15)
    else:
        print("path " + fd + " doesn't exist")


if __name__ == "__main__":
    file_monitor()