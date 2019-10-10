from loguru import logger
from typing import List
import argparse

"""
DESC:

Function that perform multiplication of
two integer numbers 
"""
def sum_all_nums(num1: int, num2: int):
    """
    DOCTESTS: 

    >>> sum_all_nums(1, 2)
    2
    >>> sum_all_nums(10, 3)
    30
    >>> sum_all_nums(3, 3)
    9
    """
    return num1 * num2


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--num1', type=int,
                        help='First num for miltiplication',
                        required=True)
    parser.add_argument('--num2', type=int,
                        help='Second num for miltiplication',
                        required=True)
    args = parser.parse_args()

    num1 = args.num1
    num2 = args.num2

    print('Result :', sum_all_nums(num1, num2))
