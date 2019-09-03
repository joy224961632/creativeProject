import os
import time
from time import sleep
import datetime

#os.system("start face.bat")
times = datetime.datetime.now()
update_Souce = open("updatetime.txt","w")
update_Souce.write(str(times))
time.sleep(3)
tall_Souce = open("tall.txt","r")
tall_data = tall_Souce.read()
face = open("face/face.txt","r")
face_data = tall_Souce.read()
print(times,tall_data)
print(tall_data)
HTMLval = '<!doctype html><html lang="en"><head><title></title><!-- Required meta tags --><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"><!-- Bootstrap CSS --><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous"><link rel="stylesheet" href="./style.css" crossorigin="anonymous"></head><body><h1 id="h1"></h1><div class="crowd1"><p class="text" id="text">'+str(tall_data)+'</p><p id="dectect"></p><p id="face">'+str(face_data)+'</p></div></br><p class="text hidden" id="time">'+str(times)+'</p><div id="footer"></div><script src="./node_modules/jquery/dist/jquery.min.js"></script></script><script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script><script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script><script src="./app.js"></script></body></html>'
web = open("index.html","w")
web.write(HTMLval)
