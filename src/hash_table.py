from typing import Any


class HashTable:
    start_table = [None] * 8

    def __init__(self):
        self.table: list[tuple[str, Any] | None] = self.start_table.copy()

    @property
    def capacity(self):
        return len(self.table)

    def __increase_capacity(self):
        self.table += self.start_table.copy()

    def __setitem__(self, key: str, value):
        index = self.hash_str(key) % self.capacity
        if self.table[index]:
            while self.table[index]:
                if self.table[index][0] == key:
                    break
                index += 1
                if index > self.capacity:
                    self.__increase_capacity()
        self.table[index] = key, value

    def __getitem__(self, item: str):
        return self.table[self.__find_element_index(item)][1]

    def __delitem__(self, key: str):
        index = (self.__find_element_index(key)+1) % self.capacity
        while self.table[index]:
            self.table[index-1] = self.table[index]
            index += 1
            index %= self.capacity
        self.table[(index-1) % self.capacity] = None

    def __find_element_index(self, key):
        index = self.hash_str(key) % self.capacity
        if not self.table[index]:
            raise KeyError()
        if self.table[start_index := index][0] != key:
            while not self.table[index] or self.table[index][0] != key:
                index += 1
                index %= self.capacity
                if index == start_index:
                    raise KeyError()
        return index

    @staticmethod
    def hash_str(string: str):
        if string == '':
            return 0
        if len(string) == 1:
            return ord(string)
        return ord(string[0])*33 + ord(string[1])

    def __iter__(self):
        return iter(key[0] for key in self.table if key)
