import pyqrcode
import png
from pyqrcode import QRCode
link=input("ENTER LINK :")
download=pyqrcode.create(link)
download.png("next_coders.png",scale=4)
print("Downloaded..")
