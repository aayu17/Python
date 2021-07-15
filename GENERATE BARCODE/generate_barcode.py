from barcode import EAN13
from barcode.writer import ImageWriter
number = "847381956139"
my_code = EAN13(number, writer=ImageWriter())
my_code.save("my_bar")
