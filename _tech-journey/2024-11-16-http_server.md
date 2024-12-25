---
layout: post
title:  HTTP Server
date:   2024-11-16
categories: [http]
---

# HTTP Server

When I think about web, my first thought come to a server. A connection between the network and software. No matter how complex system, typically it is a thread listening on a TCP socket for incoming requests. This was the case across the HTTP protocol from its first version `HTTP 0.9` until `HTTP-3` when TCP was replaced by UDP based protocol [QUIC](https://developer.mozilla.org/en-US/docs/Glossary/QUIC) protocol. You can read more about `HTTP-3` in [rfc9114](https://www.rfc-editor.org/rfc/rfc9114.html) 

It receives meta information about the request and expected response in [headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) specifying what is expected encoding, whether the request is authenticated, or should be cached.

We receive a 

```python
import http.server
import socketserver

PORT = 3000


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('X-ACTION', 'tea')
        self.end_headers()
        self.wfile.write(b'Hello, World!')


if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Serving at port", PORT)
        httpd.serve_forever()
```