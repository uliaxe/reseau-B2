import asyncio
import aioconsole

IP = "10.1.1.10"
PORT = 13337

async def async_input(writer):
    while True:
        message = await aioconsole.ainput("Enter message: ")
        writer.write(message.encode())
        await writer.drain()

async def async_receive(reader):
    while True:
        data = await reader.read(1024)
        if not data:
            break
        print(data.decode())

async def main():
    reader, writer = await asyncio.open_connection(host=IP, port=PORT)

    try:
        await asyncio.gather(async_input(writer), async_receive(reader))
    except KeyboardInterrupt:
        pass
    finally:
        writer.close()
        await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
