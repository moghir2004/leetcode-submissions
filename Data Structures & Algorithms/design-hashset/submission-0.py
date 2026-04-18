class MyHashSet:
    def __init__(self):
        self.hset = set()

    def add(self, key: int) -> None:
        if self.contains(key):
            return None
        else:
            self.hset.add(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hset.remove(key)
        else:
            return None
        

    def contains(self, key: int) -> bool:
        return True if key in self.hset else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)