class max_heap:
    def __init__(self):
        self.data = [0]

    def insert(self, num):
        self.data.append(num)
        i = len(self.data) - 1

        while i > 1:
            if self.data[i] > self.data[i // 2]:
                self.data[i], self.data[i // 2] = self.data[i // 2], self.data[i]
                i = i // 2
            else:
                break

    def remove(self):
        if len(self.data) == 1:
            data = 0
        else:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.max_heapify(1)

        return data

    def max_heapify(self, index):
        left = 2 * index
        right = 2 * index + 1
        max_index = index

        if left < len(self.data) and self.data[max_index] < self.data[left]:
            max_index = left
        if right < len(self.data) and self.data[max_index] < self.data[right]:
            max_index = right

        if max_index != index:
            self.data[index], self.data[max_index] = self.data[max_index], self.data[index]
            self.max_heapify(max_index)


import sys

if __name__ == "__main__":
    mh = max_heap()
    n = int(sys.stdin.readline())
    for i in range(n):
        x = int(sys.stdin.readline())
        if x == 0:
            print(mh.remove())
        elif x > 0:
            mh.insert(x)
