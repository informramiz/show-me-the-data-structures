**My Reasoning:** As groups can contain sub-groups and those sub-groups more sub-groups and so on so recursive approach is a perfect fit here. My code searches through groups recursively and check if user is inside of any group or sub-group.

**Time Complexity:** Let's say the max groups inside any group is (recursive tree width) `w` and and the maximum depth of any group (depth of recursive tree) is `d` then time complexity for this task is `O(w*d)`

**Space Complexity:** My solution never stores anything explicitly and only space used is due to recursion (call stack), so space complexity is `O(n)` where n is the maximum depth of a any group (depth of recursion tree).