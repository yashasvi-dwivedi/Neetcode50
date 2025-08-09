class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


if __name__ == "__main__":
    nums = list(map(int, input("Enter a list of numbers: ").split(",")))
    print("Longest consecutive is: ", Solution().longestConsecutive(nums))
