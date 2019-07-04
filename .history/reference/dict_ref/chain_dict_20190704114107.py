import collections


def main():
    a = {"a": "A", "c": "C"}
    b = {"b": "B", "c": "D"}
    m = collections.ChainMap(a, b)
    print(m)


if __name__ == "__main__":
    main()
