import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import pathlib
import json
import datetime
data_dict_1 = None

d = {}

#with open('c:/Users/IJHEA/Documents/Python/home_task_4/front-init/storage/data.json', 'r') as fil:
s = open('c:/Users/IJHEA/Documents/Python/home_task_4/front-init/storage/data.json')
d(s)    
s.close()
print(d)


