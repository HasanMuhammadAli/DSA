'''
Name: Muhammad Ali Mosin Hasan
Date: 26/6/25
Problem: 705: Design HashSet
'''

class MyHashSet:

    def __init__(self):
        self.list = []
    
    def add(self, key: int) -> None:
        if key not in self.list:
            self.list.append(key)
            #print(f"Added {key} to the set.")

    def remove(self, key: int) -> None:
        if key in self.list:
            self.list.remove(key)
            #print(f"Removed {key} from the set.")

    def contains(self, key: int) -> bool:
        return key in self.list
        


#test cases
myHashSet = MyHashSet()
myHashSet.add(1)
myHashSet.add(2)
myHashSet.contains(1)
myHashSet.contains(3)
myHashSet.add(2)
myHashSet.contains(2)
myHashSet.remove(2)