import sys
sys.path.append('src')
from scLogic import scLogic


years = [2011, 2012, 2013, 2014]


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    print("Hello World!")
    logic = scLogic()
    for year in years:
        logic.run(year)


if __name__ == "__main__":
    main()
