class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        
        A = [[] for i in range(len(nums)+1)]

        for num in count.keys():
            A[count[num]].append(num)
        res =[]
        for i in range(len(A)-1,0,-1):
            for num in A[i]:
                res.append(num)
                if len(res) == k:
                    return res