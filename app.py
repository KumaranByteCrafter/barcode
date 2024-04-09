#install barcode Module
from barcode import EAN13
from barcode.writer import ImageWriter
#number_of_barcodes - which ask the how many barcodes need to generate
num_of_barcodes = int(input("how many Barcodes you need ?"))
numbers =range(num_of_barcodes)
#loop the need of id,my_code,name to genrate the seperate barcode continously
for i in numbers:
    id = input("Give 12-digit numbers for your barcode id: ")
    my_code = EAN13(id, writer=ImageWriter)
    name = input("Give name to save barcodes")
    my_code.save(name)
