from glob import glob
import os

filenames = glob("Wechat*")

for filename in filenames:
    
    newfilename = filename.split('G')[1]
    if len(newfilename) < 8:
        newfilename = "0" + newfilename
    os.rename(filename, newfilename)