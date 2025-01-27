from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import parse_qs

'''
    Metreyle is goreller e ? en yaxsisi paputudu
'''

class Paputu(BaseHTTPRequestHandler):
    routes = {}

    @classmethod
    def get(cls, path: str, callback: callable) -> None:
        '''
            Save Callback method for URL
        '''
        cls.routes[path] = callback
        print(f"Route {path} added.")

    @classmethod
    def post(cls, path, callback):
        cls.routes[path] = callback
        print(f"Route {path} added.")


    def do_GET(self):
        try:
            handler = self.routes.get(str(self.path))

            if handler:
                handler(self)
            else:
                self.serve_static_page("framework/404.html", 404)
        except Exception as e:
            print(f"An error occurred while processing the request: {e}")

    def do_POST(self):
        try:
            handler = self.routes.get(self.path)

            if handler:
                # Parse application/x-www-form-urlencoded enctype 
                content_length = int(self.headers["Content-Length"])
                post_data = self.rfile.read(content_length)
                
                data = parse_qs(post_data.decode("utf-8"))

                handler(self, data)
            else:
                print("No handler found for the requested path. Please check the route.")
        except Exception as e:
            print(f"Error occurred in do_POST: {e}")
    
    def serve_static_page(self, filepath: str, response_code=200) -> None:
        '''
            Serve Only static page.
        '''
        try:
            with open(filepath, 'r', encoding="utf-8") as f:
                content = f.read()
            self.send_response(response_code)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))
        except FileNotFoundError:
            self.send_error(404, "File not found")
    pass

    @classmethod
    def run(cls, port:int = 8000, server_url:str = "", server_class=HTTPServer, handler_class = None):
        '''
        Leave the server_url param empty if you want to run the server locally (on your machine).
        '''
        if handler_class is None:
            handler_class = cls
            
        server_adress = (server_url, port)
        httpd = server_class(server_adress, handler_class)
        print(f"Server run on {"http://localhost:" + str(port) if server_url == "" else server_url + str(port)}")
        httpd.serve_forever()

    @staticmethod
    def test():
        print("This is test Function")


