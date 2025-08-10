#!/usr/bin/env python3
"""CountedIterator - Keeping Track of Iteration"""


class CountedIterator:
    """Custom iterator that counts how many items were iterated"""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)  # Raises StopIteration if no more items
        self.count += 1
        return item

    def get_count(self):
        """Return number of items iterated"""
        return self.count
