import asyncio
import datetime
import uvloop

uvloop.install()


def print_now():
    print(datetime.datetime.now())


def hog():
    sum = 0
    for i in range(10_000):
        for j in range(10_000):
            sum += j

    print(f"sum : {sum}")
    return sum


def trampoline(name: str = "") -> None:
    print(name, end=" ")
    print_now()

    loop.call_later(0.5, trampoline, name)


loop = asyncio.get_event_loop()


def main():
    loop.call_soon(print_now)
    loop.call_soon(print_now)

    # loop.run_until_complete(asyncio.sleep(2))

    loop.call_soon(trampoline, "one")
    # loop.call_soon(trampoline, "two")
    # loop.call_soon(trampoline, "three")

    loop.call_later(5, hog)

    loop.call_later(8, loop.stop)
    loop.set_debug(True)
    print(loop)
    loop.run_forever()


if __name__ == "__main__":
    main()
