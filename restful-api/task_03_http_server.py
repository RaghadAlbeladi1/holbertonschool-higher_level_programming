import http.server
import json



class web(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        
        
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode())
        
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()
            dat = {"version": "1.0", "description": "A simple API built with http.server"}
            json_dat = json.dumps(dat)
            self.wfile.write(json_dat.encode())

        
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")
        
            


    



def run_code(port=8000):
    server = http.server.HTTPServer(("", port),web)
    server.serve_forever()



if __name__ == "__main__":
    run_code()
