import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from http import HTTPStatus
#import ssl

class NoListingSimpleHTTPRequestHandler(SimpleHTTPRequestHandler):
    def send_head(self):
        path = self.translate_path(self.path)
        if os.path.isdir(path):
            self.send_error(HTTPStatus.FORBIDDEN, "Forbidden")
            return None
        return super(NoListingSimpleHTTPRequestHandler, self).send_head()

try:
    addr = sys.argv[1]
    port = int(sys.argv[2])
except IndexError:
    addr = '0.0.0.0'
    port = 8080

httpd = HTTPServer((addr, port), NoListingSimpleHTTPRequestHandler)

#certfile, keyfile = sys.argv[2:4]
#httpd.socket = ssl.wrap_socket(httpd.socket, server_side=True,
#        certfile=certfile, keyfile=keyfile)

print("Serving HTTP on", addr, "port", port, "...")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nKeyboard interrupt received, exiting.")
    httpd.server_close()

