class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue

            L, r = i + 1, len(nums) - 1
            while L < r:
                threeSum = a + nums[L] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    L += 1
                else:
                    res.append([a, nums[L], nums[r]])
                    L += 1
                    r -= 1
                    while L < r and nums[L] == nums[L - 1]:
                        L += 1
        return res


if __name__ == "__main__":
    print("Enter a list of numbers:")
    nums = list(map(int, input().split()))
    print("Output: ", Solution().threeSum(nums))
