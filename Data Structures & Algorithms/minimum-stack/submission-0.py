class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        del self.stack[len(self.stack) - 1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        minn = self.stack[0]
        for i in self.stack:
            if i < minn:
                minn = i
        return minn
