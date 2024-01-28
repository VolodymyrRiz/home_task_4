# ДЗ 4
import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import pathlib
import json
import datetime
import socket


class WebDodatok_HT4(BaseHTTPRequestHandler):
    
    def do_GET(self):
        pr_url = urllib.parse.urlparse(self.path)
        if pr_url.path == '/':
            self.send_html_file('index.html')
        elif pr_url.path == '/message.html':
            self.send_html_file_1('message.html')
        else:
            self.send_html_file_2('error.html', 404)
            
    def send_html_file(self, file, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open("c:/Users/IJHEA/Documents/Python/home_task_4/front-init/index.html", 'rb') as file:
            self.wfile.write(file.read())
        
    def send_html_file_1(self, file, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open("c:/Users/IJHEA/Documents/Python/home_task_4/front-init/message.html", 'rb') as file:
            self.wfile.write(file.read())
            
            
    def send_html_file_2(self, file, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open("c:/Users/IJHEA/Documents/Python/home_task_4/front-init/error.html", 'rb') as file:
            self.wfile.write(file.read())
            
            
    def do_POST(self):
        data_dict_1 = {}           
            
        data = self.rfile.read(int(self.headers['Content-Length']))
        
        print(data)
        data_parse = urllib.parse.unquote_plus(data.decode())
        print(data_parse)
        data_dict = {key: value for key, value in [el.split('=') for el in data_parse.split('&')]}
        print(data_dict)
        with open('c:/Users/IJHEA/Documents/Python/home_task_4/front-init/storage/data.json', 'r') as fil:
            data_dict_1 = json.load(fil)
            
        print(data_dict_1)    
            
        data_dict_1.update({str(datetime.datetime.now()): data_dict})
        with open('c:/Users/IJHEA/Documents/Python/home_task_4/front-init/storage/data.json', 'w', encoding='utf-8') as fil:
            json.dump(data_dict_1, fil)
        self.send_response(302)
        self.send_header('Location', '/')
        self.end_headers()
    
def run_server():
    address = ('localhost', 3000)
    http_server = HTTPServer(address, WebDodatok_HT4)
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()
        
if __name__ == '__main__':
    run_server()
    