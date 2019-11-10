#python实现二叉堆

class BinHeap():
    def __init__(self):
        self.binHeap = [0]
        self.binHeapCount = 0

    def insertNode(self, item):
        self.binHeap.append(item)
        self.binHeapCount += 1
        self.adjustInsert(self.binHeapCount)

    def findMin(self):
        return None if self.isEmpty() else self.binHeap[1]

    def isEmpty(self):
        return True if len(self.binHeap) == 1 else False

    def delMin(self):
        if self.isEmpty():
            return None
        else:
            result = self.binHeap[1]
            self.binHeap[1] = self.binHeap[-1]
            self.binHeap.pop()
            self.adjustDel(1)
            return result

    def adjustInsert(self, i):
        if i // 2 > 0:
            if self.binHeap[i // 2] > self.binHeap[i]:
                self.binHeap[i // 2], self.binHeap[i] = self.binHeap[i], self.binHeap[i // 2]
                self.adjustInsert(i // 2)

    # 直接和子节点中最小值交换，而不是只要小于子节点就交换
    def adjustDel(self, i):
        mc = self.minChild(i)
        if i * 2 < self.binHeapCount:
            if self.binHeap[mc] < self.binHeap[i]:
                self.binHeap[mc], self.binHeap[i] = self.binHeap[i], self.binHeap[mc]
                self.adjustDel(mc)

    def minChild(self, i):
        #注意判断右子节点的存在性
        if i * 2 + 1 > self.binHeapCount:
            return i * 2
        else:
            if self.binHeap[i * 2] < self.binHeap[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    #根据最小二叉堆的定义，父节点总小于子节点，因此，我们只关注有子节点的部分，也就是非叶子节点。所以只需要对数组的前半部分进行调整即可
    def buildHeap(self, alist):
        i = len(alist) // 2
        self.binHeapCount = len(alist)
        self.binHeap = [0] + alist[:]
        while(i > 0):
            self.adjustDel(i)
            i -= 1
