from datetime import datetime as dt
import hashlib


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = f"{str(self.data)}-{str(self.previous_hash)}".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __str__(self):
        return f"{self.timestamp} - {self.data}"


class Blockchain:
    def __init__(self):
        self.head = None

    def add_block(self, data):
        if self.head is None:
            temp_block = Block(dt.utcnow(), data, "0")
            self.head = temp_block
        else:
            previous_block = self.head
            while previous_block.next:
                previous_block = previous_block.next

            temp_block = Block(dt.utcnow(), data, previous_block.hash)
            temp_block.previous_hash = previous_block.hash
            previous_block.next = temp_block

    def __str__(self):
        traverse_block = self.head
        total_str = ""
        while traverse_block:
            total_str = total_str + traverse_block.__str__() + "\n"
            traverse_block = traverse_block.next
        return total_str


# Test #1: Previous Hash = hash of head
print(f"\n{'#' * 10} Test #1 {'#' * 10} ")
blkchain = Blockchain()
blkchain.add_block(data="genesis")
blkchain.add_block(data="test_1")
print(f"head->next->previous_hash == head.hash = {blkchain.head.next.previous_hash == blkchain.head.hash}")
# Output: head->next->previous_hash == head.hash = True

# Test #2: Empty Blockchain
print(f"\n{'#' * 10} Test #2 {'#' * 10} ")
blkchain = Blockchain()
print(f"Blockchain is empty: {blkchain.head is None}")
# Output: Blockchain is empty: True

# Test #3: Validity of Blockchain
print(f"\n{'#' * 10} Test #3 {'#' * 10}")
blkchain = Blockchain()
blkchain.add_block(data="genesis")
blkchain.add_block(data="test_3")
blkchain.head.data = "not_genesis"
print(f"Is Blockchain valid?: {blkchain.head.next.previous_hash == blkchain.head.calc_hash()}")
# Output: Is Blockchain valid?: False

# Test #4: Inserting Null values
print(f"\n{'#' * 10} Test #4 {'#' * 10}")
blkchain = Blockchain()
blkchain.add_block(data=None)
print(f"head->data: {blkchain.head.data}")
# Output: head->data: None
