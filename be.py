import asyncio
from abc import ABC, abstractmethod


class RequestHandler(ABC):
    @abstractmethod
    async def handle_request(self, request_data):
        pass


class HTTPRequestHandler(RequestHandler):
    async def handle_request(self, request_data):
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

    async def start(self):
        server = await asyncio.start_server(
            self.handle_client_connection, self.host, self.port
        )
        addr = server.sockets[0].getsockname()
        print(f"Serving on {addr}")

        async with server:
            await server.serve_forever()

    async def handle_client_connection(self, reader, writer):
        data = await reader.read(1024)
        address = writer.get_extra_info("peername")
        print(f"Accepted connection from {address[0]}")
        print(f"Received request:\n{data.decode('utf-8')}")

        response = await self.request_handler.handle_request(data)
        writer.write(response)
        await writer.drain()
        print("Replied with a hello message")
        writer.close()


async def main():
    host = "localhost"
    port = 8080
    request_handler = HTTPRequestHandler()
    server = Server(host, port, request_handler)
    await server.start()


if __name__ == "__main__":
    asyncio.run(main())
