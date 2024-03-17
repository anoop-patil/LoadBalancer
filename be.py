import socket
from abc import ABC, abstractmethod


# Define an abstract class for handling client requests
class RequestHandler(ABC):
    @abstractmethod
    def handle_request(self, request_data):
        pass


# Implement a specific request handler
class HTTPRequestHandler(RequestHandler):
    def handle_request(self, request_data):
        http_response = """\
HTTP/1.1 200 OK

Hello From Backend Server
"""
        return http_response.encode("utf-8")


class Server:
    def __init__(self, host, port, request_handler):
        self.host = host
        self.port = port
        self.request_handler = request_handler

    def start(self):
        with socket.socket(
            socket.AF_INET, socket.SOCK_STREAM
        ) as server_socket:
            server_socket.bind((self.host, self.port))
            server_socket.listen(5)
            print(f"Server listening on {self.host}:{self.port}...")

            while True:
                client_socket, address = server_socket.accept()
                print(f"Accepted connection from {address[0]}")
                self.handle_client_connection(client_socket)

    def handle_client_connection(self, client_socket):
        try:
            request = client_socket.recv(1024)
            print(f"Received request:\n{request.decode('utf-8')}")
            response = self.request_handler.handle_request(request)
            client_socket.sendall(response)
            print("Replied with a hello message")
        finally:
            client_socket.close()


def main():
    host = "localhost"
    port = 8080
    request_handler = HTTPRequestHandler()
    server = Server(host, port, request_handler)
    server.start()


if __name__ == "__main__":
    main()
