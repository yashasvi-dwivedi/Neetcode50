import heapq


class Solution:
    def TopKFrequent(self, nums, k):
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


if __name__ == "__main__":
    nums = list(
        map(int, input("Enter list of numbers seperated by commas: ").split(","))
    )
    k = int(input("Enter a number k: "))
    print("Top K frequent elements are: ", Solution().TopKFrequent(nums, k))
