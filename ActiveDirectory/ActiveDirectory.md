# Active Directory

### Data Structure Used
Queue

### Algorithm Used
Iterative Approach

### Complexity of the implemented Algorithm
   - is_user_in_group: O(n)
        - _n_ is the total number of all level of children.
   - Space: O(n)
        - _n_ is the total number of all level of children.

### Reasoning
This problem was very similar to iterative approach for Graph Traversal by **Breadth First Search**.
First I used Tail Recursion, but apparently python doesn't support Tail Recursion Optimization.

Queue was used, for faster adding and deleting elements as its complexity for Insert and Delete is O(1).

Also, the problem have some features:
1. Parent contains Child of same type (child group inside parent group)
2. And a termination condition (If the group is empty or we have traversed through all the elements of the group)
