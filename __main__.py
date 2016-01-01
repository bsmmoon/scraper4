import sys

from scLogic import scLogic


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    print("Hello World!")
    logic = scLogic()
    logic.run()


if __name__ == "__main__":
    main()
