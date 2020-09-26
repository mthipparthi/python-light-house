import sys

import argparse


def main():

    # print(f"Hello mate - {sys.argv[1]}")

    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    args = parser.parse_args()

    print(f"Hello mate - {args.name}")


if __name__ == "__main__":
    main()
