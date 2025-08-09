class Solution:
    def productExceptSelf(self, nums):
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


if __name__ == "__main__":
    nums = list(
        map(int, input("Enter list of integers seperated by commas ").split(","))
    )
    print("Product except self is: ", Solution().productExceptSelf(nums))
