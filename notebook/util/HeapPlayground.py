class Heap(list):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.heapify()

    def _floatup(self, pos):
        parentpos = (pos - 1) // 2
        while parentpos >= 0:
            if self[pos] < self[parentpos]:
                self[pos], self[parentpos] = self[parentpos], self[pos]
                pos, parentpos = parentpos, (parentpos - 1) // 2
                continue
            break

    def _sinkdown(self, pos, endpos):
        while pos <= (endpos - 1) // 2:
            leftchild, rightchild = pos * 2 + 1, pos * 2 + 2
            if rightchild > endpos or self[leftchild] < self[rightchild]:
                minchild = leftchild
            else:
                minchild = rightchild
            if self[pos] >= self[minchild]:
                self[pos], self[minchild] = self[minchild], self[pos]
                pos = minchild
                continue
            break

    def heappop(self):
        self[0], self[len(self) - 1] = self[len(self) - 1], self[0]
        value = self.pop()
        self._sinkdown(0, len(self) - 1)
        return value

    def heappush(self, item):
        self.append(item)
        self._floatup(pos=len(self) - 1)

    def heapify(self):
        n = len(self)
        for pos in reversed(range(n // 2)):
            self._sinkdown(pos, len(self) - 1)

if __name__ == "__main__":
    import heapq
    heap = Heap([9, 8, 7, 6, 5, 4, 3, 2, 1])
    print(heap)
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    heapq.heapify(arr)
    print(arr)
