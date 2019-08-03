import os
import base64
startup=0
people=''
Stop_Souce = open("Stop.txt","r")
Stop_data = Stop_Souce.read()
print("Programe Start")
i=0
print("Dectecting Change")
count = 0
while True:
    File_Souce = open("Upload.png","br")
    image_data = File_Souce.read()
    while True:
        status_Souce = open("status.txt","r")
        status_data = status_Souce.read()
        check_Souce = open("check.txt","r")
        check_data = check_Souce.read()
        File_Souce2 = open("Upload.png","br")
        image_data2 = File_Souce2.read()
        start_Souce = open("Start.txt","r")
        start_data = start_Souce.read()
        if(status_data == start_data):
            if(image_data != image_data2):
                print("Dectect For Change Prepareing For Upload Files...")
                tall_Souce = open("tall.txt","r")
                tall_data = tall_Souce.read()
                os.system("python update.py")
                #os.system("surge ./")
                print("Upload Success!")
                break    
        if(status_data==Stop_data):
                print("Programe Shutdonw")
                os.system("call-shutdown.bat")
                os._exit(0)