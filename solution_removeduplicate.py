class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        NAME : Remove Duplicates from Sorted Array
        LINK :
        https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/
        DESC:
        Given a sorted array nums, remove the duplicates in-place such that
        each element appear only once and return the new length.
        Do not allocate extra space for another array, you must do this by modifying
        the input array in-place with O(1) extra memory.

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
        i = 0
        while i < len(nums):
            if nums[i] in nums[i+1:]:
                for n in range(nums[i+1:].count(nums[i])):
                    nums.pop(i)
            i += 1
        return len(nums)

if __name__ == "__main__":
    """
    if call:
    python -m doctest -v solution_removeduplicate.py
    – will run doctest
    """
    import doctest
    doctest.testmod()
    import logging
    logging.basicConfig(filename="sample.log", level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--nums', nargs='+',
                        help='List of sorted values',
                        required=True)
    nums = parser.parse_args().nums

    logger.info(u'Got array from command line arguments : {nums}')
    logger.info(u'Removing duplicates ...')

    res = removeDuplicates(nums)

    logger.info(u'...Done')

    print('Result length :', res)
    print('Result array :', nums)


