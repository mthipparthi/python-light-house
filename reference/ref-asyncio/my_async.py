import time
import asyncio


async def heartbeat():
    while True:
        start = time.time()
        await asyncio.sleep(1)
        delay = time.time() - start - 1
        print(f"heartbeat delay = {delay:.3f}s")


def main():
    asyncio.run(heartbeat())

    loop = asyncio.get_event_loop()
    loop.call_later(10, loop.stop)
    loop.run_until_complete()


if __name__ == "__main__":
    main()
