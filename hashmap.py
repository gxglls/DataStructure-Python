u# python使用hash表实现map,使用线性探测发处理哈希冲突
class HashMap():
    def __init__(self, size):
        self.size = size
        self.keyList = [None] * size
        self.valList = [None] * size

    def hashFunc(self, val):
        return val % self.size

    def put(self, key, val):
        slot = self.hashFunc(key)
        temp = slot
        while self.keyList[slot] and self.keyList[slot] != key:
            slot +=1
            if slot % self.size == temp:
                return "no space!"
        self.keyList[slot] = key
        self.valList[slot] = val

    def get(self, key):
        slot = self.hashFunc(key)
        temp = slot
        while self.keyList[slot] and self.keyList[slot] != key:
            slot += 1
            if slot % self.size == temp:
                return "not found!"
        if self.keyList[slot] == key:
            return self.valList[slot]
        else:
            return "not found"

    def getStatus(self):
        return self.keyList,self.valList



ins = HashMap(11)
print(ins.put(11,"a"))
print(ins.put(13,"b"))
print(ins.put(22,"b"))
print(ins.put(33,"b"))
print(ins.put(30,"c"))
print(ins.put(41,"c"))
print(ins.get(11))
print(ins.getStatus())
