# Taro 75 -- Fast Track

> A curated shortcut through the full Taro 75 problem set. Master the top patterns, then work the two problem lists in order: the first 10 give you 80% coverage, the full 20 give you 99%.

---

## Top 10 Patterns

These are the most frequently used techniques across all 75 problems, ranked by how often they appear.

| Rank | Pattern | Frequency | When to reach for it |
|------|---------|-----------|----------------------|
| 1 | **Hash Map / Hash Set** | ~22 problems | You need O(1) lookup, counting, grouping, or duplicate detection. The single most versatile tool in interviews. |
| 2 | **Two Pointers** | ~15 problems | The input is sorted (or can be), and you need to find pairs, partition, or shrink a search range from both ends. |
| 3 | **Greedy** | ~14 problems | A locally optimal choice at each step leads to a globally optimal result. Often paired with sorting. |
| 4 | **DFS / Recursion / Backtracking** | ~10 problems | You are exploring trees, graphs, grids, or need to enumerate all valid configurations (subsets, permutations, paths). |
| 5 | **Sorting** | ~8 problems | Used as a preprocessing step to enable two pointers, greedy merging, or to group related elements together. |
| 6 | **Stack / Monotonic Stack** | ~8 problems | You need to match nested structures (parentheses, calculators) or find the next greater/smaller element efficiently. |
| 7 | **Linked List Manipulation** | ~7 problems | Pointer reversal, merge, copy, or cycle detection on singly/doubly linked lists. Practice the dummy-node technique. |
| 8 | **Dynamic Programming** | ~7 problems | The problem has overlapping subproblems and optimal substructure. Look for "minimum cost," "number of ways," or "longest/shortest" in the prompt. |
| 9 | **Binary Search** | ~6 problems | The search space is monotonic. Works on sorted arrays, rotated arrays, and "search on answer" problems where you binary search a value range. |
| 10 | **Sliding Window** | ~6 problems | You need the best/smallest/longest contiguous subarray or substring satisfying a constraint. Expand the right end, shrink the left. |

---

## 10 Problems -- 80% Coverage

These 10 problems teach the core patterns that recur across the majority of the Taro 75. Solve them first.

| # | Problem | Difficulty | Pattern(s) | Why this problem |
|---|---------|------------|------------|------------------|
| 1 | **1. Two Sum** | Easy | Hash Map | The quintessential hash map problem; the "complement lookup" idea reappears in dozens of variants. |
| 2 | **15. 3Sum** | Medium | Two Pointers, Sorting | Teaches sorting as a prerequisite, two-pointer convergence, and duplicate skipping -- a pattern used in 4Sum, Container With Most Water, and more. |
| 3 | **3. Longest Substring Without Repeating Characters** | Medium | Sliding Window, Hash Set | The textbook sliding window: expand right, shrink left when a constraint breaks. Directly transfers to Minimum Window Substring. |
| 4 | **200. Number of Islands** | Medium | DFS, Matrix Traversal | Grid-based DFS is the foundation for Rotting Oranges, Word Search, and any "connected component" problem. |
| 5 | **70. Climbing Stairs** | Easy | Dynamic Programming | The simplest DP recurrence (Fibonacci-style). Builds intuition for House Robber, Coin Change, and all tabulation problems. |
| 6 | **20. Valid Parentheses** | Easy | Stack | Classic stack matching. The same push/pop discipline applies to calculators, decode strings, and simplify path. |
| 7 | **33. Search in Rotated Sorted Array** | Medium | Binary Search | Forces you to handle a non-trivial binary search invariant. Generalizes to Find Peak Element and Koko Eating Bananas. |
| 8 | **206. Reverse Linked List** | Easy | Linked List Manipulation | The fundamental pointer-swap loop. The reversal technique is a subroutine in Merge k Sorted Lists and Add Two Numbers. |
| 9 | **56. Merge Intervals** | Medium | Sorting, Greedy | Sort then greedily merge -- a template for all interval problems and a common system-design building block. |
| 10 | **121. Best Time to Buy and Sell Stock** | Easy | Greedy | Track a running minimum and maximize the gap. Introduces greedy single-pass thinking used in Jump Game and Candy. |

> **Patterns covered:** Hash Map, Two Pointers, Sorting, Sliding Window, DFS, Matrix Traversal, Dynamic Programming, Stack, Binary Search, Linked List, Greedy.

---

## 20 Problems -- 99% Coverage

The 10 above plus 10 more that fill the remaining gaps: advanced versions of the core patterns, plus niche techniques (backtracking, monotonic deque, topological sort, design, divide and conquer).

### Core 10 (from above)

| # | Problem | Pattern(s) |
|---|---------|------------|
| 1 | **1. Two Sum** | Hash Map |
| 2 | **15. 3Sum** | Two Pointers, Sorting |
| 3 | **3. Longest Substring Without Repeating Characters** | Sliding Window, Hash Set |
| 4 | **200. Number of Islands** | DFS, Matrix Traversal |
| 5 | **70. Climbing Stairs** | Dynamic Programming |
| 6 | **20. Valid Parentheses** | Stack |
| 7 | **33. Search in Rotated Sorted Array** | Binary Search |
| 8 | **206. Reverse Linked List** | Linked List Manipulation |
| 9 | **56. Merge Intervals** | Sorting, Greedy |
| 10 | **121. Best Time to Buy and Sell Stock** | Greedy |

### Additional 10

| # | Problem | Difficulty | Pattern(s) | Why this problem |
|---|---------|------------|------------|------------------|
| 11 | **42. Trapping Rain Water** | Hard | Advanced Two Pointers | The hardest two-pointer problem. Two converging pointers with running maxima -- a technique that appears nowhere else but is an interview favorite. |
| 12 | **76. Minimum Window Substring** | Hard | Sliding Window, Hash Map | The most demanding sliding window problem. Teaches the "valid window" contraction pattern with frequency maps. |
| 13 | **207. Course Schedule** | Medium | Graph DFS, Topological Sort | Introduces adjacency-list graphs and cycle detection. Directly extends to Course Schedule II (topological ordering). |
| 14 | **79. Word Search** | Medium | Backtracking, Matrix | Pure backtracking on a grid with in-place visited marking. Covers the recursion + undo pattern missing from the core 10. |
| 15 | **322. Coin Change** | Medium | DP (unbounded knapsack) | A different DP shape than Climbing Stairs: iterate over items and amounts. Generalizes to Word Break and Longest Increasing Subsequence. |
| 16 | **146. LRU Cache** | Medium | Design, Hash Map, Linked List | The premier data-structure design problem. Combines a hash map with a doubly linked list for O(1) get/put. |
| 17 | **239. Sliding Window Maximum** | Hard | Monotonic Deque | Introduces the monotonic deque -- a specialized structure for range-max/min queries in O(n). Also strengthens Daily Temperatures intuition. |
| 18 | **4. Median of Two Sorted Arrays** | Hard | Advanced Binary Search | The hardest binary search problem in the set. Teaches partitioning two arrays simultaneously in O(log min(m, n)). |
| 19 | **23. Merge k Sorted Lists** | Hard | Divide and Conquer, Linked List | Pairwise merging in O(N log k). Teaches the divide-and-conquer merge pattern that scales to external sort and map-reduce. |
| 20 | **347. Top K Frequent Elements** | Medium | Heap / Bucket Sort, Hash Map | Covers the "top K" archetype using frequency counting + bucket sort. Transfers to Kth Largest Element and Reorganize String. |

> **Additional patterns covered:** Advanced Two Pointers, Advanced Sliding Window, Topological Sort, Backtracking, Unbounded Knapsack DP, Data Structure Design, Monotonic Deque, Advanced Binary Search, Divide and Conquer, Heap / Bucket Sort.

---

> **Study order:** Work the 10-problem list first, then the additional 10. After that, mop up the remaining 55 problems by category -- the patterns will already feel familiar.
