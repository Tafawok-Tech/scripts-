import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import PyPDF2
import os, os.path
import glob
import threading
import sched
import requests
import re
import win32print
import shutil
import win32api
import PyPDF2

class Watcher:
    DIRECTORY_TO_WATCH = "printer-lis/"

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
            # Take any action here when a file is first created.
            #print("Received created event - %s." % event.src_path)
            time.sleep(3)
            list = os.listdir('printer-lis')
            print(list)
            pdf_dir="printer-lis"
            number_files = len(list)
            if number_files > 0:
                for k in range(0,number_files):
                    string1 = 'printer-lis'
                    string = 'printer-lis/' + str(list[k])
                    f = open(string, 'rb')
                    fileReader = PyPDF2.PdfFileReader(f)
                    title=fileReader.getDocumentInfo()["/Title"]
                    f.close()
                    if title == "Barcodes":
                        win32print.SetDefaultPrinter('zebraa')
                    else:
                        win32print.SetDefaultPrinter('HP LaserJet Professional P1102 (Copy 1)')

                    print("printing file "+ string +" on "+str(win32print.GetDefaultPrinter()))
                    win32api.ShellExecute(0, "print", os.path.join(string1,str(list[k])), None,  ".",  0)
            time.sleep(3)

            files = glob.glob('printer-lis/*')
            for f in files:
                os.remove(f)

        #elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            #print("Received modified event - %s." % event.src_path)




if __name__ == '__main__':
    w = Watcher()
    w.run()
