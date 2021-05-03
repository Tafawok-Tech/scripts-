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
            #temp=[]
            #time.sleep(10)
            #file_size = -1
            #temp=os.path.getsize(event.src_path)
            #print(temp)
            #while file_size != os.path.getsize(event.src_path):
                #file_size = os.path.getsize(event.src_path)
                #time.sleep(1)
            time.sleep(1)
            #list = os.listdir('printer-lis')
            list_of_files = glob.glob('printer-lis/*')
            #number_files = len(list)
            #if number_files > 0:
                #while ".crdownload" in list[0] or ".tmp" in list[0]:
                    #list = os.listdir('printer-lis')
            #print(list)
            latest_file = max(list_of_files, key=os.path.getctime)
            latest_file_name = os.path.basename(latest_file)
            while ".pdf" not in latest_file_name:
                list_of_files = glob.glob('printer-lis/*')
                latest_file = max(list_of_files, key=os.path.getctime)
                latest_file_name = os.path.basename(latest_file)
                time.sleep(1)
            list_of_files = glob.glob('printer-lis/*')
            latest_file = max(list_of_files, key=os.path.getctime)
            latest_file_name = os.path.basename(latest_file)
            #if latest_file_name not in temp
            #temp.append(latest_file_name)
            print(latest_file_name)
            string1 = 'printer-lis'
            string = 'printer-lis/' + latest_file_name
            my_printer = "HP LaserJet Professional P1102 (Copy 1)"
            #if not temp:
            win32api.ShellExecute (0, "print",os.path.join(string1,latest_file_name) , my_printer, ".", 0)
            #pdf_dir="printer-lis"
            
            #number_files = len(list)
            #if number_files > 0:
                #for k in range(0,number_files):
                    #string1 = 'printer-lis'
                    #string = 'printer-lis/' + str(list[k])
                    #string3 = 'C:/Users/HP/Downloads/printer-lis/' + str(list[k])
                    #string3='C:\Users\HP\Downloads\printer-lis/' + str(list[k])
                    #f = open(string, 'rb')
                    #fileReader = PyPDF2.PdfFileReader(f)
                    #title=fileReader.getDocumentInfo()["/Title"]
                    #print(title)
                    #f.close()
                    #my_printer = "HP LaserJet Professional P1102 (Copy 1)"
                    #acrobat = "C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe"
                    #call([acrobat, "/T", string3, my_printer])
                    #print("printing file "+ string +" on "+my_printer)
                    #win32api.ShellExecute (0, "print",os.path.join(string1,str(list[k])) , my_printer, ".", 0)
                    #win32print.SetDefaultPrinter('HP LaserJet Professional P1102 (Copy 1)')
                    #currentprinter = win32print.GetDefaultPrinter()
                    #print(currentprinter)
                    #print("printing file "+ string +" on "+str(win32print.GetDefaultPrinter()))
                    #win32api.ShellExecute(0, "print", os.path.join(string1,str(list[k])), currentprinter,  ".",  0)
                    #win32api.ShellExecute(0, "print", os.path.join(string1,str(list[k])), None,  ".",  0)
                    #time.sleep(5)

            #time.sleep(20)
            #files = glob.glob('printer-lis/*')
            #for f in files:
                #os.remove(f)

        #elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            #print("Received modified event - %s." % event.src_path)




if __name__ == '__main__':
    w = Watcher()
    w.run()
