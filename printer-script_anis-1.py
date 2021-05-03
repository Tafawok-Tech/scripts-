import os, os.path
import threading
import sched, time
import requests
import glob
import re
import win32print
import time
import shutil
import win32api
import PyPDF2

s = sched.scheduler(time.time, time.sleep)
old_number = 0
def do_something(sc, old_number): 
    
    # path joining version for other paths
    list = os.listdir('printer-lis') # dir is your directory path
    number_files = len(list)
    list_of_files = glob.glob('printer-lis/*')
    if number_files > 0:
        latest_file = max(list_of_files, key=os.path.getctime)
        latest_file_name = os.path.basename(latest_file)
        if "pdf" not in latest_file_name: 
            print('invalid file format exists')
            f = open('printer-lis/' + latest_file_name)
            f.close()
            os.remove('printer-lis/*')
            do_something(sc, old_number)
        print(os.path.basename(latest_file))
        print(number_files)
        try:
            f = open('printer-lis/' + latest_file_name, 'rb')
            fileReader = PyPDF2.PdfFileReader(f)
            title=fileReader.getDocumentInfo()["/Title"]
            f.close()
            print('File exists')
        except FileNotFoundError:
            print('File does not exist')
        # check if any new files were added
        if number_files > old_number :
            #files = {'upload_file': ('test_doc.png', open(r"printer-lis/" + latest_file_name,'rb'))}
            #os.startfile(os.path.normpath("printer-lis/" + latest_file_name), "print")
            #all_printers = win32print.EnumPrinters(2)
            defaultPrinter = win32print.GetDefaultPrinter()
            print(defaultPrinter)
            if defaultPrinter != 'HP LaserJet Professional P1102 (Copy 1)':
                win32print.SetDefaultPrinter('HP LaserJet Professional P1102 (Copy 1)')
            if title == "Barcodes": #"barcode" in latest_file_name: 
                win32print.SetDefaultPrinter('zebraa')
            pdf_dir = 'printer-lis'
            while True:
                files = os.listdir(pdf_dir)
                if len(files) > 0:
                    for f in files:
                        print("printing file "+ str(pdf_dir+f) +" on "+str(win32print.GetDefaultPrinter()))
                        win32api.ShellExecute(0, "print", os.path.join(pdf_dir,f), None,  ".",  0)
                        time.sleep(6)
                        os.remove(os.path.join(pdf_dir,f))
                        #os.remove('printer-lis/*')
                        do_something(sc, old_number)
                else:
                    time.sleep(3)
                    do_something(sc, old_number)
        else:
            print('no new files added')
        time.sleep(3)
        do_something(sc, old_number)
    else:
        print('empty folder')
        time.sleep(3)
        do_something(sc, old_number)
s.enter(1, 1, do_something, (s,old_number))
s.run()
