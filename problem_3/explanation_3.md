**My Reasoning:** My implementation is based on explanation from [this](https://en.wikipedia.org/wiki/Huffman_coding) Wikipedia link so most of the guideline for data structures came from there. 

1. I have used `PriorityQueue` as in when building the tree we always need the 2 minimum frequency elements which fits perfectly with `PriorityQueue`. 
2. Then to get code for each letter we need to traverse the tree as letters are at leaves of the tree and `recursion` fits perfectly for this type of tree traversal and so I have used recursion to generate letter codes.
3. To maintain letter frequencies and codes I have used `dict` for fast access.

**Time Complexity:**

1. For encoding
	- Count frequencies, `O(n)`
	- Building the huffman tree uses _Priority Queue_ which takes `O(lgn)` for insertion so for all insertions it will take `O(nlgn)`.
	- Finding the letter codes is done using tree traversal, height of tree is `lg(n)` and width at max `n` so total `O(nlgn)`
	- Coverting data into codes is `O(n)` 
	- Total cost is `O(nlgn)`
2. For decoding, it is just a loop that goes through the coded data length so `O(n)`
3. Total cost is `O(nlgn)`

	
**Space Complexity:** All the data storage is in terms of input (tree, frequency count, letter codes) and it is always linear, `O(n)`.