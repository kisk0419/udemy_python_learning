"""
socket server and web browser

use webbrowser from console

> import webbrowser
> webbrowser.open([url])

way to use firefox

> f = webbrowser.get('firefox)
> f.open([url])

"""
import http.server
import socketserver


with socketserver.TCPServer(('127.0.0.1', 8080), http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()