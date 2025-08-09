class Solution:
    def twoSum(self, nums, target):
        pair_idx = {}
        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [pair_idx[target - num], i]
            pair_idx[num] = i
        return []


if __name__ == "__main__":
    nums = list(
        map(int, input("Enter a list of numbers seperated by spaces: ").split())
    )
    target = int(input("Enter a target: "))
    print("The pair that satifies the target is: ", Solution().twoSum(nums, target))
