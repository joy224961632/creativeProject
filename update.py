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
face_data = face.read()
print(face_data)
print(times,tall_data)
print(tall_data)
HTMLval = '<!doctype html>\n<html lang="en">\n<head>\n<title></title>\n<!-- Required meta tags -->\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\n<!-- Bootstrap CSS -->\n<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">\n<link rel="stylesheet" href="./style.css" crossorigin="anonymous">\n</head>\n<body>\n<h1 id="h1"></h1>\n<div class="crowd1">\n<p class="text" id="text">'+str(tall_data)+'</p>\n<p id="dectect"></p>\n<p id="face">'+str(face_data)+'</p>\n</div>\n</br>\n<p class="text hidden" id="time">'+str(times)+'</p>\n<div id="footer"></div>\n<script src="./node_modules/jquery/dist/jquery.min.js"></script>\n<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>\n<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>\n<script src="./app.js"></script>\n</body>\n</html>'
web = open("index.html","w")
web.write(HTMLval)
