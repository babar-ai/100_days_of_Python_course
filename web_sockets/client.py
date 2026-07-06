import asyncio
import websockets

async def main():

    uri = "ws://localhost:8000/ws"

    async with websockets.connect(uri) as websocket:

        await websocket.send("Hello Server")

        response = await websocket.recv()

        print(response)

asyncio.run(main())