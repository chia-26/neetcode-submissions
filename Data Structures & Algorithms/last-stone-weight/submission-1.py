class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def helper(stones):
            stones.sort()
            if len(stones) == 1:
                return stones[0]
            if len(stones) == 0:
                return 0
            
            if stones[-1] > stones[-2]:
                print(1)
                stones[-1] = stones[-1] - stones[-2]
                stones.remove(stones[-2])
            elif stones[-2] < stones[-1]:
                print(2)
                stones[-2] = stones[-2] - stones[-1]
                stones.remove(stones[-1])
            elif stones[-2] == stones[-1]:
                print(3)
                stones.remove(stones[-1])
                stones.remove(stones[-1])

            print(stones)
            return helper(stones)

        return helper(stones)