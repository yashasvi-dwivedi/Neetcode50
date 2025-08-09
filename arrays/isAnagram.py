class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


if __name__ == "__main__":
    s = input("Enter a string: ")
    t = input("Enter another string: ")
    print("Is it anagram?", Solution().isAnagram(s, t))
