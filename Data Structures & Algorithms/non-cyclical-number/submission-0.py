class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []

        def helper(n, seen):
            print("n: ", n)
            if n == 1:
                return True
            summ = 0
            for i in str(n):
                print("i: ", i)
                summ += int(i)**2
            if summ in seen:
                return False
            seen.append(summ)
            return helper(summ, seen)
        
        return helper(n, seen)
