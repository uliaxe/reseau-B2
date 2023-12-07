import asyncio

async def handle_client(reader, writer):
    client_address = writer.get_extra_info('peername')
    print(f"Client connected from {client_address[0]}:{client_address[1]}")

    data = await reader.read(1024)
    message = data.decode()
    print(f"Received message from client: {message}")

    response = f"Hello {client_address[0]}:{client_address[1]}"
    writer.write(response.encode())
    await writer.drain()

    writer.close()

async def start_server():
    server = await asyncio.start_server(
        handle_client, '10.1.2.20', 13337)

    addr = server.sockets[0].getsockname()
    print(f"Server listening on {addr[0]}:{addr[1]}")

    async with server:
        await server.serve_forever()

asyncio.run(start_server())
