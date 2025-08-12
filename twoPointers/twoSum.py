class Solution:
    def twoSum(self, nums, target):
        L, r = 0, len(nums) - 1

        while L < r:
            curSum = nums[L] + nums[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                L += 1
            else:
                return [L + 1, r + 1]
        return []


if __name__ == "__main__":
    print("Enter a list of numbers:")
    nums = list(map(int, input().split()))
    print("Enter a target: ")
    target = int(input())
    print("Output:", Solution().twoSum(nums, target))
