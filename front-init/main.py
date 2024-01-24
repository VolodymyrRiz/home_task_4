# ДЗ 4
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import pathlib

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
            print('jkkjkjkjkjkjkkk')
            
    def send_html_file_2(self, file, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open("c:/Users/IJHEA/Documents/Python/home_task_4/front-init/error.html", 'rb') as file:
            self.wfile.write(file.read())
            print('2222222222222222222222')
            
    def do_POST(self):
        pass
    
def run_server():
    address = ('localhost', 3000)
    http_server = HTTPServer(address, WebDodatok_HT4)
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()
        
if __name__ == '__main__':
    run_server()
    