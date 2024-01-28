# ДЗ 4
import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
from pathlib import Path
import logging
import json
import datetime
import socket
from threading import Thread

BASE_DIR = Path()
BUFFER_SIZE = 1024
HTTP_PORT = 3000
SOCKET_PORT = 5000
HTTP_HOST = 'localhost'
SOCKET_HOST = "127.0.0.1"


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
        data = self.rfile.read(int(self.headers['Content-Length']))        
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.sendto(data, (SOCKET_HOST, SOCKET_PORT))
        client_socket.close()
        self.send_response(302)
        self.send_header('Location', '/')
        self.end_headers()
        
        
def save_data_from_form(data):
    data_dict_1 = {}  
    data_parse = urllib.parse.unquote_plus(data.decode())
    
    data_dict = {key: value for key, value in [el.split('=') for el in data_parse.split('&')]}
   
    with open('c:/Users/IJHEA/Documents/Python/home_task_4/front-init/storage/data.json', 'r') as fil:
        data_dict_1 = json.load(fil)            
              
    data_dict_1.update({str(datetime.datetime.now()): data_dict})
    with open('c:/Users/IJHEA/Documents/Python/home_task_4/front-init/storage/data.json', 'w', encoding='utf-8') as fil:
        json.dump(data_dict_1, fil)
        
        
def run_socket_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    
    logging.info('Starting socket server!')
    try:
        while True:
            msg, address = server_socket.recvfrom(BUFFER_SIZE)
            save_data_from_form(msg)
            logging.info(f"Socket received {address}: {msg}")
        
    except KeyboardInterrupt:
        server_socket.close()
    
    
def run_http_server(host, port):
    address = (host, port)
    http_server = HTTPServer(address, WebDodatok_HT4)
    logging.info('Starting http server!')
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()
        
        
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    
    server = Thread(target=run_http_server, args=(HTTP_HOST, HTTP_PORT))
    server.start()
    
    server_socket = Thread(target=run_socket_server, args=(SOCKET_HOST, SOCKET_PORT))
    server_socket.start()