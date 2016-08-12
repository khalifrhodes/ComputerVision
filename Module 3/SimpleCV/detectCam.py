import subprocess
from SimpleCV import Image
import time

subprocess.call("raspistill -n -w %s -h %s -o Listing1_1.bmp"%(640,480), shell=True)

img = Image("Listing1_1.bmp")
img.show()

pixel=img[120,200]

print pixel

img[120,200]=(0,0,0)

pixel=img[120,200]

img.save("Listing1_2.bmp")

print pixel