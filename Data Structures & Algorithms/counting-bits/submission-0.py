class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for j in range(n+1):
            count = 0
            for i in range(10):
                if (1<<i) & j > 0:
                    print(int(bin(j)[2:]))
                    count += 1
                    print("Count: ", count)
            ans.append(count)
        return ans
