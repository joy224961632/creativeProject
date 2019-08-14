import os
import base64
stop = 0
print("Start")
print("Loading Files... Please Wait")
start_Souce = open("Start.txt","r")
start_data = start_Souce.read()
print("Start Sign Get!")
print("Dectec Start Sign")
while (True):
    status_Souce = open("Status.txt","r")
    status_data = status_Souce.read()
    if(status_data == start_data and stop ==0):
        stop = 1
        #os.system("")
        os.system("call-start.bat")
        os.system("python joy-creative-project-update-programe.py")
        break
