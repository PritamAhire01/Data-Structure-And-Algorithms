class Solution:
    def twoSum(self, nums, target):
        """
        Returns indices of the two numbers in 'nums' that add up to 'target'.
        """
        num_to_index = {}  # Maps number to its index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i

        # The problem guarantees exactly one solution, so this line is optional
        return []
