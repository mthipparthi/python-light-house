import collections


def main():
    a = {"a": "A", "c": "C"}
    b = {"b": "B", "c": "D"}
    m = collections.ChainMap(a, b)
    print(m)
    print('Individual Values')
    print('a = {}'.format(m['a']))
    print('b = {}'.format(m['b']))
    print('c = {}'.format(m['c']))
    print()

    print('Keys = {}'.format(list(m.keys())))
    print('Values = {}'.format(list(m.values())))
    print()

if __name__ == "__main__":
    main()
