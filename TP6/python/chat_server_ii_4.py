import asyncio

global CLIENTS
CLIENTS = {}

async def handle_client(reader, writer):
    client_address = writer.get_extra_info('peername')
    print(f"Received connection from {client_address}")

    if client_address in CLIENTS:
        print(f"Client {client_address} is already connected. Ignoring.")
        writer.close()
        return

    CLIENTS[client_address] = {}
    CLIENTS[client_address]["r"] = reader
    CLIENTS[client_address]["w"] = writer

    try:
        while True:
            data = await reader.read(1024)
            if not data:
                break
            message = data.decode()

            for addr, client_info in CLIENTS.items():
                if addr != client_address:
                    ip, port = addr
                    broadcast_message = f"\n{ip}:{port} said: {message}"
                    client_info["w"].write(broadcast_message.encode())
                    await client_info["w"].drain()

    finally:
      
        print(f"Connection from {client_address} closed.")
        del CLIENTS[client_address]
        writer.close()

async def main():
    server = await asyncio.start_server(
        handle_client, '10.1.2.20', 13337)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
