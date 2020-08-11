"""
Name: David Stacey
Student ID: 001260498
Class: C950
"""


class Table:
    # initialize empty list
    # O(n) -- constant
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = []
        # fill with empty list
        for _ in range(capacity):
            self.table.append([])

    # create hash key based off of given key to determine list position
    # O(n) -- constant
    def get_hash(self, key):
        hash_key = hash(key) % self.capacity
        return hash_key

    # figures out where value is stored and the inserts it
    # O(1) -- constant
    def insert(self, key, value):
        # calls get_hash method to get a unique hash key
        bucket = self.get_hash(key)
        self.table[bucket].append([key, value])
        self.size += 1

    # O(n)
    def get(self, key):
        bucket = self.get_hash(key)
        if self.table[bucket] is not None:
            bucket_list = self.table[bucket]
            # O(n) -- for loop
            for index, value in bucket_list:
                if index == key:
                    return value
        else:
            print("Not found.")
            return None

    # O(n^2) -- for loop nested in another for loop
    def get_all(self):
        package_list = []
        # O(n) -- for loop
        for bucket in self.table:
            # O(n) -- for loop
            for item in bucket:
                package_list.append(item[1])
        return package_list

    # O(1) -- constant
    def get_size(self):
        return self.size
