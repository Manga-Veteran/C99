import os
import shutil
path = 'C:/Users/anlyc'
print("before copying files:")
print(os.listdir(path))
source = "C:/Users/anlyc/epik.txt"
destination = "C:/Users/anlyc/epik(copy).txt"
dest = shutil.copy(source, destination)
print("after copying files")
print(os.listdir(path))