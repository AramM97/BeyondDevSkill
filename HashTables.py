class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (existing_key, _) in enumerate(self.table[index]):
                if existing_key == key:
                    # If key already exists, update the value
                    self.table[index][i] = (key, value)
                    break
            else:
                # If key doesn't exist, append a new key-value pair
                self.table[index].append((key, value))

    def delete(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for i, (existing_key, _) in enumerate(self.table[index]):
                if existing_key == key:
                    del self.table[index][i]
                    break

    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for existing_key, value in self.table[index]:
                if existing_key == key:
                    return value
        return None

if __name__ == "__main__":
    # Test HashTable
    print("Testing HashTable:")
    hash_table = HashTable(size=5)

    # Insert values
    hash_table.insert(123, 28)
    hash_table.insert(456, 35)
    hash_table.insert(789, 42)

    # Search values
    print("Search values:")
    print("Value associated with key 123:", hash_table.search(123))  # Should print 28
    print("Value associated with key 456:", hash_table.search(456))  # Should print 35
    print("Value associated with key 789:", hash_table.search(789))  # Should print 42
    print()

    # Update existing value
    print("Update existing value:")
    hash_table.insert(123, 30)
    print("Updated value associated with key 123:", hash_table.search(123))  # Should print 30
    print()

    # Delete a key
    print("Delete a key:")
    hash_table.delete(456)
    print("Value associated with key 456 after deletion:", hash_table.search(456))  # Should print None
    print()

    # Test collision handling
    print("Testing collision handling:")
    hash_table.insert(101, 25)
    hash_table.insert(201, 23)
    print("Value associated with key 101:", hash_table.search(101))  # Should print 25
    print("Value associated with key 201:", hash_table.search(201))  # Should print 23
    print()

    # Test non-existent key
    print("Testing non-existent key:")
    print("Value associated with key 999:", hash_table.search(999))  # Should print None
