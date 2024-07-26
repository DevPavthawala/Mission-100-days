# getting ascii value

# def get_hash(key):
#     h = 0
#     for char in key:
#         h += ord(char)
#         return h % 100

# print(get_hash('march 6'))
# print(ord('m'))

class HashTable:
    def __init__(self):
        self.Max =  10
        self.arr = [[] for i in range(self.Max)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
            return h % self.Max

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key,value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


t = HashTable()

t['march 6'] = 190
t['april 25'] = 110
t['march 1'] = 120
t['dec 31'] = 130

print(t.get_hash('march 6'))
print(t.get_hash('march 1'))

print(t.arr)

del t['dec 31']

print(t.arr)