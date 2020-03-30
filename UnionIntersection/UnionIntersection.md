# Union-Intersection
### Algorithms used
Sequential traversal and comparison.

### Assumptions Made
1. Since Union and Intersection are Set operation, the list have no duplicates, if they have only unique values will be selected.

### Complexity for data structures
- Singly LinkedList
    - Insert: O(n)
    - Space:  O(n)

### Complexity of the implemented Data Structure
   - union:         O(m * n)
        - m and n sizes of the two Linked Lists
   - intersection:  O(m * n)
        - m and n sizes of the two Linked Lists

### Reasoning
I chose LinkedList for two reasons:
1. It was mentioned in the project to use it
2. I could have used HashTable or Set internally, but then 
    - It would not be Space Optimized
    - Using Set data structure would have defeated the purpose of implementing these two algorithms
