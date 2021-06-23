import os
import http.server
import socketserver

from urlparse import urlparse, parse_qs
from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        msg = query_components["msg"] 
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        msg = 'Hello! you sent %s' % (msg)
        self.wfile.write(msg.encode())


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
