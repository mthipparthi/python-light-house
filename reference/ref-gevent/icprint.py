from icecream import ic


def foo(i):
    return i + 333


d = {"key": {1: "one"}}


if __name__ == "__main__":
    ic(foo(123))
    ic(d)
