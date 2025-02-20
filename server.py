import os
from http.server import HTTPServer, CGIHTTPRequestHandler
from socket import socket

os.system("clear")
os.mkdir('DARK_SERIES_XYLON')
   
def find_free_port():
    """Finds a random available port."""
    with socket() as s:
        s.bind(('', 0))
        return s.getsockname()[1]


def start_server(codex):

    
    """Starts an HTTP server for the given codex."""
    os.chdir(codex)
    port = find_free_port()

    # Configure CGIHTTPRequestHandler
    handler = CGIHTTPRequestHandler
    handler.cgi_directories = ["/cgi-bin"]  # Set a specific codex for CGI scripts

    # Create the server
    
    
    httpd = HTTPServer(('localhost', port), handler)
    print(f"Server running on http://localhost:{port}")
    print(f"Server running on http://localhost:{port}")
    print("Press Ctrl+C to stop the server.")
    httpd.serve_forever()


if __name__ == "__main__":
    try:
        codex = "DARK_SERIES_XYLON".strip()
        if os.path.isdir(codex):
            start_server(codex)
        else:
            print("Invalid codex path. Please try again.")
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
