class Solution:
    def isPalindrome(self, s):
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]


if __name__ == "__main__":
    s = input("Enter a Sentence: ")
    print("The given string is a palindrome: ", Solution().isPalindrome(s))
