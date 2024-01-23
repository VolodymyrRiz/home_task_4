# ДЗ 4
from http.server import HTTPServer, BaseHTTPRequestHandler


class WebDodatok_HT4(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'hhhhhh')
        
            
    def do_POST(self):
        pass
    
def run_server():
    address = ('localhost', 8080)
    http_server = HTTPServer(address, WebDodatok_HT4)
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()
        
if __name__ == '__main__':
    run_server()