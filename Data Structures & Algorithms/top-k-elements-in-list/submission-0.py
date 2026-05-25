class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [7,7]
        counter = {}
        res = []
        buckets = [[] for n in range(len(nums) + 1)]
        for i in range(len(nums)):
            counter[nums[i]] = 1 + counter.get(nums[i], 0)
        # { 7: 2 }
        for key in counter:
            buckets[counter[key]].append(key)
        # [[], [], [7]]
        for i in range(len(buckets) - 1, 0, -1):
            while len(buckets[i]) > 0:
                res.append(buckets[i].pop())
                if len(res) == k:
                    return res
        return res
