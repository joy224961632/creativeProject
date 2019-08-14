import os
import shutil
import time
i=0
while(True):
    status_Souce = open("status.txt","r")
    status_data = status_Souce.read()
    stop_Souce = open("Stop.txt","r")
    stop_data = stop_Souce.read()
    shutil.copyfile('face/1.jpg','face/test.jpg')
    print("Done1")

    time.sleep(1)
    shutil.copyfile('face/2.jpg','face/test.jpg')
    print("Done2")

    time.sleep(1)

    i+=1
    if(status_data == stop_data or i > 10):
        print("Done")
        break
