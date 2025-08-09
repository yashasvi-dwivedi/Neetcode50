class Solution:
    def hasDuplicate(self, nums):
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False


if __name__ == "__main__":
    nums = list(map(int, input("Enter list of numbers separated by space: ").split()))
    print("Has Duplicate: ", Solution().hasDuplicate(nums))
