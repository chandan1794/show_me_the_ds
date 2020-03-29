class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(f"Node Value: {self.value}")


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value)
            if cur_head.next:
                out_string += " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def find(self, ele):
        temp_node = self.head
        while temp_node:
            if temp_node.value == ele:
                return True
            temp_node = temp_node.next
        return False


def union(llist_1, llist_2):
    union_list = LinkedList()

    for ll in [llist_1, llist_2]:
        temp_node = ll.head
        while temp_node:
            if not union_list.find(temp_node.value):
                union_list.append(temp_node.value)
            temp_node = temp_node.next

    return union_list


def intersection(llist_1, llist_2):
    intersection_list = LinkedList()

    temp_node = llist_2.head
    while temp_node:
        if llist_1.find(temp_node.value) and not intersection_list.find(temp_node.value):
            intersection_list.append(temp_node.value)
        temp_node = temp_node.next

    return intersection_list


# Test #1: One list is Empty
print(f"\n{'#' * 10} Test #1 {'#' * 10} ")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = []

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(f"Union: {union(linked_list_1, linked_list_2)}")
# Output: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21
print(f"Intersection: {intersection(linked_list_1, linked_list_2)}")
# Output:

# Test #2: Both lists are empty
print(f"\n{'#' * 10} Test #2 {'#' * 10} ")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()
element_1 = []
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(f"Union: {union(linked_list_3, linked_list_4)}")
# Output:
print(f"Intersection: {intersection(linked_list_3, linked_list_4)}")
# Output:

# Test #3: Both lists are mutually exclusive
print(f"\n{'#' * 10} Test #3 {'#' * 10} ")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()
element_1 = [1, 2, 3, 4, 5]
element_2 = [6, 7, 8, 9, 10]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(f"Union: {union(linked_list_3, linked_list_4)}")
# Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
print(f"Intersection: {intersection(linked_list_3, linked_list_4)}")
# Output:

# Test #4: Both lists have same elements (not necessarily in the same order)
print(f"\n{'#' * 10} Test #4 {'#' * 10} ")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()
element_1 = [1, 2, 3, 4, 5]
element_2 = [5, 4, 3, 2, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(f"Union: {union(linked_list_3, linked_list_4)}")
# Output: 1 -> 2 -> 3 -> 4 -> 5
print(f"Intersection: {intersection(linked_list_3, linked_list_4)}")
# Output: 5 -> 4 -> 3 -> 2 -> 1
