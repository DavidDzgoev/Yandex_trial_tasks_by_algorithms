class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def main():
    number = input()
    if abs(int(number)) > 10000:
        return

    S = Stack()

    if number[0] == '-':
        answer = '-'
        number = number.replace('-', '')
    else:
        answer = ''

    for i in number:
        S.push(i)

    if S.peek() == '0' and S.size() != 1:
        while S.peek() == '0':
            S.pop()

    while not S.isEmpty():
        answer = answer + S.pop()

    print(answer)


main()
