from collections import deque


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.size = 0
        self.lru = {}
        self.cache_order = deque()

    def get(self, key):
        try:
            value = self.lru[key]
            self.cache_order.popleft()
            self.cache_order.append(key)
            return value
        except Exception as e:
            return -1

    def set(self, key, value):
        if self.capacity > self.size:
            self.lru[key] = value
            self.cache_order.append(key)
            self.size = self.size + 1
        else:
            lru_key = self.cache_order.popleft()
            del self.lru[lru_key]
            self.lru[key] = value
            self.cache_order.append(key)


# Preparing Initial Data for tests
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

# Test #1: Cache Hit
print(f"\n{'#' * 10} Test #1 {'#' * 10} ")
print(our_cache.get(1))
# Output: 1

# Test #2: Cache Miss
print(f"\n{'#' * 10} Test #2 {'#' * 10} ")
print(our_cache.get(9))
# Output: -1
# Because 9 is not present in the cache

# Test #3: Cache Overflow
print(f"\n{'#' * 10} Test #3 {'#' * 10} ")
our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(2))
# Output: -1
# Because the cache reached it's capacity and 2 was the least recently used entry

# Test #4: Empty Key: Cache Miss
print(f"\n{'#' * 10} Test #4 {'#' * 10} ")
print(our_cache.get(""))
# Output: -1
# Because the key doesn't exists

# Test #5: Null Key: Cache Miss
print(f"\n{'#' * 10} Test #5 {'#' * 10} ")
print(our_cache.get(None))
# Output: -1
# Because the key doesn't exists
