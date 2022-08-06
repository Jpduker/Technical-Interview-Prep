class stack:
    def __init__(self):
        self.capacity = 5
        self.stack = []*self.capacity

    def push(self, data):
        if not self.isFull():
            self.stack.append(data)
        else:
            print("stack is full")

    def isFull(self):
        return len(self.stack) == self.capacity

    def isEmpty(self):
        return len(self.stack) == 0

    def pop(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            print("Stack is empty")

    def printStack(self):
        for i in self.stack:
            print(i)

    def test(self):
        st = stack()
        print(st.isEmpty())

        print(" ")
        st.push(5)
        st.push(7)
        st.push(10)
        st.push(29)
        st.push(32)

        st.printStack()
        print(" ")
        st.push(4)

        print(" ")
        st.printStack()
        print(" ")
        st.pop()
        print(" ")
        st.printStack()
        print(" ")
        st.isFull()

        print(" ")
        st.printStack()


if __name__ == "__main__":
    St = stack()
    St.test()
