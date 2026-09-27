#!/usr/bin/env python3
"""
MediThread - Local Development & Production Preview Web Server
Serves static assets with proper MIME types, CORS, and fallback routing.
"""

import http.server
import socketserver
import os
import sys

PORT = 3000

class MediThreadHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS and caching headers for high performance
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.end_headers()

def run_server():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    handler = MediThreadHTTPRequestHandler
    
    # Allow port reuse
    socketserver.TCPServer.allow_reuse_address = True
    
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"============================================================")
        print(f"  MediThread Platform Server Running at:")
        print(f"  --> http://localhost:{PORT}")
        print(f"============================================================")
        print("Press Ctrl+C to stop the server.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            httpd.server_close()

if __name__ == '__main__':
    run_server()
