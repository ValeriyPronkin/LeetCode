from typing import List
import argparse

from loguru import logger


"""

NAME : Remove Duplicates from Sorted Array
LINK : https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/

DESC:

Given a sorted array nums, remove the duplicates in-place such that
each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.

"""


def remove_duplicates_from_sorted_array(nums: List[int]) -> List[int]:
    """
    >>> nums = [1, 1, 2]
    >>> remove_duplicates_from_sorted_array(nums)
    2
    >>> nums == [1, 2]
    True

    >>> nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    >>> remove_duplicates_from_sorted_array(nums)
    5
    >>> nums == [0, 1, 2, 3, 4]
    True
    """

    j = 0
    for i in range(len(nums)):
        if (nums[i-1] != nums[i]) or (i == 0):
            j += 1
    return j


if __name__ == "__main__":
    """
    if call:
    python -m doctest -v remove_duplicates_from_sorted_array.py
    – will run doctest
    """
    import doctest
    doctest.testmod()

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--nums', nargs='+',
                        help='List of sorted values',
                        required=True)
    nums = parser.parse_args().nums

    logger.info(f'Got array from command line arguments : {nums}')
    logger.info(f'Removing duplicates ...')

    res = remove_duplicates_from_sorted_array(nums)

    logger.info(f'...Done')

    print('Result length :', res)
    print('Result array :', nums)
