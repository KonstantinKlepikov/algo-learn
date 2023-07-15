"""Example of problem solution"""
from util.timer import short_timeit, long_timeit


class Solution:

    @short_timeit
    def this(self, nums: list[int], target: int) -> list[int]:
        """
        Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add
        up to target.
        You may assume that each input would have exactly one
        solution, and you may not use the same element twice.
        You can return the answer in any order.

        Example 1:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

        Example 2:
        Input: nums = [3,2,4], target = 6
        Output: [1,2]

        Example 3:
        Input: nums = [3,3], target = 6
        Output: [0,1]

        Constraints:

        2 <= nums.length <= 10^4
        -10^9 <= nums[i] <= 10^9
        -10^9 <= target <= 10^9
        Only one valid answer exists.
        """

        while True:
            n = nums.pop()
            n_ind = len(nums)

            diff = target - n

            if diff in nums:

                return [n_ind, nums.index(diff)]


if __name__ == '__main__':

    s = Solution()

    t = s.this(nums=[2, 7, 11, 15], target=9)
    assert t[0] in [0, 1]
    assert t[1] in [0, 1]
    print('-'*20)

    t = s.this(nums=[3, 2, 4], target=6)
    assert t[0] in [1, 2]
    assert t[1] in [1, 2]
    print('-'*20)

    t = s.this(nums=[3, 3], target=6)
    assert t[0] in [0, 1]
    assert t[1] in [0, 1]
    print('-'*20)

    t = s.this(nums=[3, 2, 3], target=6)
    assert t[0] in [0, 2]
    assert t[1] in [0, 2]
    print('-'*20)

    t = s.this(nums=[-3, 4, 3, 90], target=0)
    assert t[0] in [0, 2]
    assert t[1] in [0, 2]
    print('-'*20)

    long_timeit()(s.this)(nums=[2, 7, 11, 15], target=9)
