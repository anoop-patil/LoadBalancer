import asyncio
from abc import ABC, abstractmethod


class CommunicationHandler(ABC):
    @abstractmethod
    async def send(self, data):
        pass

    @abstractmethod
    async def receive(self):
        pass


class BackendCommunicationHandler(CommunicationHandler):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.reader = None
        self.writer = None

    async def connect(self):
        self.reader, self.writer = await asyncio.open_connection(
            self.host, self.port
        )

    async def send(self, data):
        self.writer.write(data)
        await self.writer.drain()

    async def receive(self):
        return await self.reader.read(1024)


class ProxyServer:
    def __init__(self, host, port, backend_host, backend_port):
        self.host = host
        self.port = port
        self.backend_handler = BackendCommunicationHandler(
            backend_host, backend_port
        )

    async def handle_client(self, reader, writer):
        data = await reader.read(1024)
        addr = writer.get_extra_info("peername")
        print(f"Received request from {addr[0]}:\n{data.decode()}")

        await self.backend_handler.connect()
        await self.backend_handler.send(data)

        backend_data = await self.backend_handler.receive()
        print("Response from server:", backend_data.decode())

        writer.write(backend_data)
        await writer.drain()
        writer.close()

    async def start(self):
        server_coro = asyncio.start_server(
            self.handle_client, self.host, self.port
        )
        server = await server_coro
        addr = server.sockets[0].getsockname()
        print(f"Serving on {addr}")

        # Keep the server running indefinitely
        await server.wait_closed()


async def main():
    host = "localhost"
    port = 80
    backend_host = "localhost"
    backend_port = 8080

    proxy_server = ProxyServer(host, port, backend_host, backend_port)
    await proxy_server.start()


if __name__ == "__main__":
    asyncio.run(main())
