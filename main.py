from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Define the custom request handler
class HeaderHandler(BaseHTTPRequestHandler):

    def handle_whoami(self):
        # Get the value of X-Auth-Username header
        username = self.headers.get('X-Auth-Username', 'Unknown')

        # Create a JSON response
        response = json.dumps({'username': username}).encode('utf-8')

        # Send the response
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(response)

    def serve_html_file(self):
        try:
            # Open the file and read its contents
            with open('index.html', 'r') as file:
                content = file.read()

            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))
        except IOError:
            # Handle file not found error
            self.send_error(404, 'File not found: index.html')

    def do_GET(self):
                # Check the path to determine the response
        if self.path == '/':
            # Serve the HTML file
            self.serve_html_file()
        elif self.path == '/whoami':
            # Handle the whoami endpoint
            self.handle_whoami()
        else:
            # Send 404 Not Found for other paths
            self.send_response(404)
            self.end_headers()
        # Set the response status code
      


# Set up the server
def run_server():
    server_address = ("", 8002)  # Use your preferred host and port
    httpd = HTTPServer(server_address, HeaderHandler)
    print(f"Server started on http://localhost:{server_address[1]}")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()