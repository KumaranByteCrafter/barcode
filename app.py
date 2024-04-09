#install barcode Module
from barcode import EAN13
from barcode.writer import ImageWriter

num_of_barcodes = int(input("how many Barcodes you need ?"))
numbers =range(num_of_barcodes)
for i in numbers:
    id = input("Give 12-digit numbers for your barcode id: ")
    my_code = EAN13(id, writer=ImageWriter)
    name = input("Give name to save barcodes")
    my_code.save(name)