import os
import time
from time import sleep
import datetime
times = datetime.datetime.now()
update_Souce = open("updatetime.txt","w")
update_Souce.write(str(times))
time.sleep(3)
tall_Souce = open("tall.txt","r")
tall_data = tall_Souce.read()
print(times,tall_data)
print(tall_data)
HTMLval = '<!doctype html>\n<html lang="en">\n<head>\n<title></title>\n<!-- Required meta tags -->\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\n<!-- Bootstrap CSS -->\n<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">\n<link rel="stylesheet" href="./style.css" crossorigin="anonymous">  \n</head>\n<body>\n<p class="text" id="text">'+ str(tall_data)   + '</p></br>\n<p class="text hidden" id="time">'+ str(times) +'</p> <img id="img" class="img" alt="" width="900px">\n<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>\n<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>\n<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>\n<script src="./app.js"></script> \n </body>\n</html>"'
web = open("index.html","w")
web.write(HTMLval)