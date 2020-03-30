# LRU Cache
### Data Structure
I used **Dictionary** as **Hash Table** for the cache.
To save the order I have user **dequeue** as **Queue**.

### Complexity for data structures
- Hashtable (Average Time Complexity)
    - Insert: O(1)
    - Delete: O(1)
    - Search: O(1)
    - Space:  O(n)

- Queue:
    - Insert: O(1)
    - Delete: O(1)
    - Space:  O(n)

### Complexity of the implemented Data Structure
   - get:   O(1)
   - set:   O(1)
   - Space: O(n)

### Reasoning
I needed to use two different data structures because, Dictionary by default is not ordered and
and List is ordered but time complexity for search is a variable of number of input elements i.e. O(n).
So, I used most useful features from both the data structures
- List as Queue: Ordered
- Dictionary as HashTable: Search O(1) (Average Time Complexity)[https://wiki.python.org/moin/TimeComplexity]
