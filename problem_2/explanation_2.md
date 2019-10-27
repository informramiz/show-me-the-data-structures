**Reasoning for Code:** As each directory can contain more directories and those directories can contain more and so on and there is no limit to depth so it perfectly fits the recursive pattern and that's why I have used a recursive function to find all matching files in current directory and do the same for all the nested directories.

**Time Complexity:** The maximum depth of recursive function is the maximum number of sub-directories, say `d` and in each call we go through all the files and directories inside the given directory say, `w` so total cost is `O(d*w)`, if can be simplified to `O(n)` where `n = d * w`

**Space Complexity:** Again, we will consider the depth of recursion which is `d` and in each call we store `w` files/directories so total space complexity is `O(d*w)`.
  