# Finding Files
### Algorithm Used
Recursion

### Complexity of the implemented Algorithm
   - find_files: O(n * l)
        - _n_ is the number of files, directories under all levels the given path
        - _l_ is the length of the suffix
   - Space: O(n)
        - _n_ is number of all the files where given suffix matches

### Reasoning
I chose Recursion because, it is a classic recursion problem. Where we do not know the depth of the problem.
We can visualize the directory as an **Acyclic Graph**. And to traverse a **Graph**, we use recursive algorithms all the time.
It is very similar to **Breadth First Search**.

Also, a Recursive problem have some features:
1. Parent contains Child of same type (child directory inside parent directory)
2. And a termination condition (If there are no more contents inside or if the current path is not a directory or we have traversed through all the contents of the given path)
