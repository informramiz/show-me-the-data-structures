**My Reasoning:** 
As union and intersection are `set` operations and set are designed to perform them efficiently so I have converted both lists to set and after performing those operations I convert the final `set` back to `LinkedList`.

**Time Complexity:**


Note: _Set_ is implemented using _HashTable_ so operations like insert, search, delete etc. take `O(1)`. [Reference](https://wiki.python.org/moin/TimeComplexity)

1. `Union:` _LinkedList_ to set conversion takes `O(n)` as _Set_ is implemented using _HashTable_, union takes `O(n1+n2) = O(n)` as you have to add elements of both lists by traversing both, total = `O(n)`
2. `Intersection:` _LinkedList_ to set conversion takes `O(n)`, intersection of two sets is `O(n1*n2)`where n1 and n2 are elements count in first and second set respectively.

**Space Complexity:** Space complexity peaks out at when taking union and is `O(n1 + n2)` and the rest of the time is equal or less than this so total space complexity is `O(n)`