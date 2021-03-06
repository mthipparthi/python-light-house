import collections


def notes():
    # 1. chainmaps - chains maps but when you access values it will pick up the first value form first map
    # 2. It works like a stack, you are effectively stacking one map on top of other.
    # 3. so it picks up values form top of the stack
    # 4. you can add new children as all get added at the top.
    pass


def basic_example():
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


def order_matters():
    a = {"a": "A", "c": "C"}
    b = {"b": "B", "c": "D"}
    m = collections.ChainMap(b, a)
    print("a = {}".format(m["a"]))
    print("b = {}".format(m["b"]))
    print("c = {}".format(m["c"]))


def dict_update():
    a = {"a": "A", "c": "C"}
    b = {"b": "B", "c": "D", "d": "E"}
    a.update(b)
    print(a)


from collections import Counter


def anagram(a, b):
    c = Counter(a)
    d = Counter(b)
    if len(c) > len(d):
        e = c - d
    else:
        e = d - c

    if not e:
        return True
    else:
        return False


if __name__ == "__main__":
    # dict_update()
    print(anagram("abc", "cbad"))
    print(anagram("abc", "bac"))
