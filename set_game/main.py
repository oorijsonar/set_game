from algorithm import BruteForce
from dealer import deal


def main():
    board = deal()
    print(BruteForce(board).find())


if __name__ == '__main__':
    main()
