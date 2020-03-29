# Huffman Coding
### Data Structure Used
Min-heap or Minimum Heap for HuffmanTree

### Complexity for data structures
- Min-heap
    - Insert: O(log(n))
    - Delete: O(log(n))
    - Search: O(n)
    - Space:  O(n)

### Complexity of the implemented Data Structure
   - huffman_encoding:  O(n * log(n))
        - There are two parts which takes this much time, created sorted frequency set from the given string and building the min-heap.
   - huffman_decoding:   O(n)
     - Will have to traverse through the whole encoded string character by character
   - Space: O(n)

### Reasoning
I chose Min-heap, because in huffman encoding we give non-uniform length codes to characters, which depends on their frequency.
So the target is to give the code of lesser length to the more frequent characters and vice versa.
In Min-heap, we have the least number at the top and then we build the tree up from there. So, in the _merge_frequencies_ step,
we merge the two least frequent node and create a new node, and push that node into the min-heap again, and so on until we are remain with only one node in the min-heap.

So, to build from bottom to up, we always need the two least frequent items, and inserting a new one, and min-heap serve the purpose very well.
