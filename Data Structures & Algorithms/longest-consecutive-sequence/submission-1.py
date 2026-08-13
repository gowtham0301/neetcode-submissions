class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        longest = 1

        for num in nums_set:
            if num - 1 not in nums_set:
                current = num
                current_length = 1

                while current + 1 in nums_set:
                    current += 1
                    current_length += 1

                longest = max(longest, current_length)

        return longest