class MinStack:

    def __init__(self) -> None:
        self.content = []
        self.minSoFar = []

    def push(self, value: int) -> None:
        self.content.append(value)
        if len(self.minSoFar) == 0:
            self.minSoFar.append(value)
            return
        self.minSoFar.append(min(value, self.minSoFar[-1]))

    def pop(self) -> None:
        self.content.pop()
        self.minSoFar.pop()

    def top(self) -> int:
        return self.content[-1]

    def getMin(self) -> int:
        return self.minSoFar[-1]


if __name__ == "__main__":
    obj = MinStack()
    obj.push(2)
    obj.push(3)
    obj.push(1)
    obj.push(5)
    obj.push(4)
    obj.pop()
    print(obj.top())
    print(obj.getMin())
