# BFS_Practice


https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/discuss/696776/BFS-Thinking-Process

This is exactly the same as the previous question binary matrix or any normal shortest paths
The k obstacles needs to be tracked which is why we need to add to visited.

If I just mark i , j as visited by mutating array I am not keepring track of k's , this combination (i,j) could be there in another path and if I see it assigned 2 i simply skip it, which is wrong, it could have a permissible k that we can explore

# That is why it is better to maintain visited where we store all 3 vals i, j, k instead of mutating array alone to 2.
