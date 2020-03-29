# Active Directory
### Algorithm Used
Recursion

### Complexity of the implemented Algorithm
   - is_user_in_group: O(n), Where _n_ is the number of groups and users in the given group.
   - Space: O(1), True/False

### Reasoning
I chose Recursion because, it is a classic recursion problem. Where we do not know the depth of the problem.
We can visualize the Group as an **Acyclic Graph**. And to traverse a **Graph**, we use recursive algorithms all the time.
It is very similar to **Breadth First Search**.

Also, a Recursive problem have some features:
1. Parent contains Child of same type (child group inside parent group)
2. And a termination condition (If the group is empty or we have traversed through all the elements of the group)
