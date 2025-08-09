from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())


if __name__ == "__main__":
    strs = [s.strip() for s in input("Enter a list of strings: ").split(",")]
    print("Anagrams are: ", Solution().groupAnagrams(strs))
