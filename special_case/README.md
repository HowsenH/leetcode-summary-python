# Special Case

The following questions, I prefer to solve by some not commonly used methods. If you interest more about those methods, please find more material about this method.

* [Topological Sort](##Topological-Sort)
* [Binary Indexed Tree](##Binary-Indexed-Tree)

## Topological-Sort

In computer science, a topological sort or topological ordering of a directed graph is a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering. [Wikipedia](https://en.wikipedia.org/wiki/Topological_sorting)

| *#* | *Link* |
| ---- | --------------------------------------------------------------------- |
| 207 | https://leetcode.com/problems/course-schedule/ |
| 210 | https://leetcode.com/problems/course-schedule-ii/ |
| 310 | https://leetcode.com/problems/minimum-height-trees/ |

## Binary-Indexed-Tree

A Fenwick tree or binary indexed tree is a data structure that can efficiently update elements and calculate prefix sums in a table of numbers. [Wikipedia](https://en.wikipedia.org/wiki/Fenwick_tree)

For my understanding, the binary indexed tree is another evolution from divided DP. However, when you want to change the preprocessing sum in divided DP, it takes O(n) time, which is not efficient in some cases. Then you may need to choose the binary indexed tree. 

| *#* | *Link* |
| ---- | --------------------------------------------------------------------- |
| 307 | https://leetcode.com/problems/range-sum-query-mutable/ |