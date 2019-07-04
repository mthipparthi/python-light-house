import collections


def notes():
    # 
    pass

def main():
    a = {"a": "A", "c": "C"}
    b = {"b": "B", "c": "D"}
    m = collections.ChainMap(a, b)
    print(m)
    print("Individual Values")
    print("a = {}".format(m["a"]))
    print("b = {}".format(m["b"]))
    print("c = {}".format(m["c"]))
    print()

    print("Keys = {}".format(list(m.keys())))
    print("Values = {}".format(list(m.values())))
    print()
    print("Items:")
    for k, v in m.items():
        print("{} = {}".format(k, v))
    print()

    print('"d" in m: {}'.format(("d" in m)))


def test():
    a = {"a": "A", "c": "C"}
    b = {"b": "B", "c": "D"}
    m = collections.ChainMap(b, a)
    print("a = {}".format(m["a"]))
    print("b = {}".format(m["b"]))
    print("c = {}".format(m["c"]))


if __name__ == "__main__":
    test()
