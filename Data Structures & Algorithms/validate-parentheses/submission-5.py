class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        arr = []
        opened = "([{"
        closed = ")]}"

        for b in s:
            if b in opened:
                arr.append(b)
            else:
                if len(arr) == 0:
                    return False
                if closed.index(b)  == opened.index(arr[len(arr) - 1]):
                    arr.pop()
                else:
                    return False
        return len(arr) == 0