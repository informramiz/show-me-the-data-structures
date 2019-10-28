**My Reasoning:** 
For union and intersection we need to know whether elements is occured at least in 1 list (union) or both (intersection) and `dict` is the right data structure to store that information due to its `O(1)` cost. So I have used a `dict` to mark items occurred. The rest is just checking of items occurence and adding items back to resultant list.

**Time Complexity:**

1. `Union:` Going through both lists to mark items takes `O(n)` and then going through all dictionary items is `O(m + n)` so total `O(m + n)`, where m and n are items in each list respectively.
2. `Intersection:` Going through both lists to mark items takes `O(n)` and then going through all dictionary items is `O(m + n)` so total `O(m + n)`, where m and n are items in each list respectively.

**Space Complexity:** Space complexity is `O(m + n)`, where m and n are items in each list respectively.