import os
from http.server import HTTPServer, CGIHTTPRequestHandler
from socket import socket
uname =input('\033[1;91m[\033[1;92m√\033[1;91m] \x1b[38;5;50mENTER YOUR NAME \033[1;91m: \33[1;32m')
import os
os.system("clear")
os.system('espeak -a 300 " What,   is,   your,   Name,"')
print("nenenennelmwm")
os.system("touch /sdcard/ DARK_SERIES_XYLON")

# check whether directory already exists

  
   
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
    
