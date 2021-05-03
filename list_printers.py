import win32api
import win32print

#file= "C:\Users\HP\Downloads\printer-lis\aaa.pdf"
# Gives me information on the printers available to me
#printers = win32print.EnumPrinters(2)

# This gives you the systems default printer
#printer_name = win32print.GetDefaultPrinter()

printer_list = []
for x in range(len(printers)):
    printer_list.append(printers[x][2])
print(printer_list)




# printer_list should look something like the example below
# ['Send To OneNote 2016', 'Microsoft XPS Document Writer', 
#  'Microsoft Print to PDF', 'Fax', 'Brother DCP-7065DN', 'Canon MAXIFY iB4120']
# 
# Let's say I want to print my text file to pdf just for fun.
#

#my_printer = "HP LaserJet Professional P1102 (Copy 1)"

# This will print to the Microsoft Print to PDF printer option
#win32api.ShellExecute (0, "print", file, my_printer, ".", 0)
# This would print it to my default printer due to the None arg
# win32api.ShellExecute (0, "print", file, None, ".", 0)


