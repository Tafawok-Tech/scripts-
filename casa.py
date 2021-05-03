import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
#import PyPDF2
import os, os.path
import glob
import threading
#import sched
#import requests
#import re
import win32print
#import shutil
import win32api


class Watcher:
    DIRECTORY_TO_WATCH = "test/"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(3)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            time.sleep(2)
            #list = os.listdir('printer-lis')
            list_of_files = glob.glob('test/*')
            latest_file = max(list_of_files, key=os.path.getctime)
            latest_file_name = os.path.basename(latest_file)
            if ".png" in latest_file_name:
                print(latest_file_name)
                files = {'upload_file': ('test_doc.png', open(r"test/" + latest_file_name,'rb'))}
                r = requests.post("http://165.22.27.138/lims/v1/histogram/submit", files= files, data={'latest_file': latest_file_name})
                print(r.json())




if __name__ == '__main__':
    w = Watcher()
    w.run()
