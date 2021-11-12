import statistics
from timeit import default_timer as timer
from copy import deepcopy
import click

import algorithm
import dealer


def list_algorithms():
    return [subclass.__name__ for subclass in algorithm.Algorithm.__subclasses__()]


def get_algorithm_class(algorithm_name):
    return getattr(algorithm, algorithm_name)


@click.command()
@click.option('-a', '--algorithm', 'algorithm_name', type=click.Choice(list_algorithms()), required=True)
@click.option('-i', '--iterations', type=int, default=1000)
def main(algorithm_name, iterations):
    deck = dealer.generate_deck()
    algorithm_class = get_algorithm_class(algorithm_name)

    times = []

    for _ in range(iterations):
        board = dealer.deal(deck)
        board_copy = deepcopy(board)
        start_time = timer()
        possible_set = algorithm_class(board_copy).find()
        end_time = timer()

        # TODO: print the board in all the assert failure messages
        if possible_set is not None:
            assert possible_set.is_set(), f'Your algorithm said it found a set but {possible_set} is not a set!'
            # TODO: check if the set is on the board
        else:
            assert algorithm.BruteForce(board).find() is None, 'Your algorithm didn\'t find a set that BruteForce did!'
        times.append(end_time - start_time)

    print(f'Average time: {statistics.mean(times) * 1000} milliseconds')


if __name__ == '__main__':
    main()
