INITIAL_CAPACITY = 10


class HashTable:
    def __init__(self):
        self.capacity = INITIAL_CAPACITY
        self.buckets = [[] for _ in range(self.capacity)]

    def hash_function(self, key):
        return key % self.capacity

    def insert(self, key, value):
        hash_index = self.hash_function(key)
        self.buckets[hash_index].append([key, value])

    def find(self, key):
        hash_index = self.hash_function(key)

        for ele_cell in self.buckets[hash_index]:
            if ele_cell[0] == key:
                return ele_cell[1]

    def remove(self, key):
        hash_index = self.hash_function(key)

        for index, ele_cell in enumerate(self.buckets[hash_index]):
            if ele_cell[0] == key:
                print("Deleting ... (", ele_cell, ")")
                del self.buckets[hash_index][index]

    def display_hash_table(self):
        for index, ele_cell in enumerate(self.buckets):
            print(index, end=" ")
            for ele in ele_cell:
                print("--> ", end=" ")
                print(ele[1], end=" ")
            print()


if __name__ == "__main__":
    hash_table = HashTable()

    hash_table.insert(10, "Allahabad")
    hash_table.insert(25, "Mumbai")
    hash_table.insert(20, "Mathura")
    hash_table.insert(9, "Delhi")
    hash_table.insert(21, "Punjab")
    hash_table.insert(31, "Noida")

    print("The Hash Table: ")
    hash_table.display_hash_table()

    print("Finding value of 20 key: ", hash_table.find(20))

    hash_table.remove(9)

    print("The Hash Table After Removing...")
    hash_table.display_hash_table()
