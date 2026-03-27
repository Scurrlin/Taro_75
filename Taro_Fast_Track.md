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
| 12 | **124. Binary Tree Maximum Path Sum** | Hard | Tree DFS, Post-Order Recursion | The quintessential binary tree DFS problem. Teaches post-order traversal, combining child results, and tracking a global optimum while returning a different value up the call stack. |
| 13 | **207. Course Schedule** | Medium | Graph DFS, Topological Sort | Introduces adjacency-list graphs and cycle detection. Directly extends to Course Schedule II (topological ordering). |
| 14 | **79. Word Search** | Medium | Backtracking, Matrix | Pure backtracking on a grid with in-place visited marking. Covers the recursion + undo pattern missing from the core 10. |
| 15 | **322. Coin Change** | Medium | DP (unbounded knapsack) | A different DP shape than Climbing Stairs: iterate over items and amounts. Generalizes to Word Break and Longest Increasing Subsequence. |
| 16 | **146. LRU Cache** | Medium | Design, Hash Map, Linked List | The premier data-structure design problem. Combines a hash map with a doubly linked list for O(1) get/put. |
| 17 | **239. Sliding Window Maximum** | Hard | Monotonic Deque | Introduces the monotonic deque -- a specialized structure for range-max/min queries in O(n). Also strengthens Daily Temperatures intuition. |
| 18 | **994. Rotting Oranges** | Medium | BFS, Matrix Traversal | Multi-source BFS on a grid -- all rotten oranges enqueued at once and spread level by level. The go-to template for shortest-path and wavefront problems. |
| 19 | **23. Merge k Sorted Lists** | Hard | Divide and Conquer, Linked List | Pairwise merging in O(N log k). Teaches the divide-and-conquer merge pattern that scales to external sort and map-reduce. |
| 20 | **347. Top K Frequent Elements** | Medium | Heap / Bucket Sort, Hash Map | Covers the "top K" archetype using frequency counting + bucket sort. Transfers to Kth Largest Element and Reorganize String. |

> **Additional patterns covered:** Advanced Two Pointers, Tree DFS / Post-Order Recursion, Topological Sort, Backtracking, Unbounded Knapsack DP, Data Structure Design, Monotonic Deque, BFS, Divide and Conquer, Heap / Bucket Sort.

---

> **Study order:** Work the 10-problem list first, then the additional 10. After that, mop up the remaining 55 problems by category -- the patterns will already feel familiar.

---

## Solutions

### 1. Two Sum

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            num2 = target - num
            if num2 in seen:
                return [seen[num2], i]
            seen[num] = i
```

### 15. 3Sum

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return res
```

### 3. Longest Substring Without Repeating Characters

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l, res = 0, 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, r - l + 1)
        return res
```

### 200. Number of Islands

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(row, col):
            if not (0 <= row < rows
                and 0 <= col < cols
                and grid[row][col] == '1'):
                return

            grid[row][col] = '0'
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    dfs(row, col)
                    islands += 1

        return islands
```

### 70. Climbing Stairs

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        one, two = 2, 1

        for _ in range(3, n + 1):
            current = one + two
            two = one
            one = current
        return one
```

### 20. Valid Parentheses

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return not stack
```

### 33. Search in Rotated Sorted Array

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
```

### 206. Reverse Linked List

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
```

### 56. Merge Intervals

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        merged = []
        for i in intervals:
            if not merged or merged[-1][1] < i[0]:
                merged.append(i)
            else:
                merged[-1][1] = max(merged[-1][1], i[1])
        return merged
```

### 121. Best Time to Buy and Sell Stock

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        best = 0
        for p in prices:
            if p < minPrice:
                minPrice = p
            else:
                best = max(best, p - minPrice)
        return best
```

### 42. Trapping Rain Water

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        h = height
        if not h:
            return 0
        l, r = 0, len(h) - 1
        leftMax, rightMax, volume = h[l], h[r], 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, h[l])
                volume += leftMax - h[l]
            else:
                r -= 1
                rightMax = max(rightMax, h[r])
                volume += rightMax - h[r]
        return volume
```

### 124. Binary Tree Maximum Path Sum

```python
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            res[0] = max(res[0], root.val + left + right)
            return root.val + max(left, right)

        dfs(root)
        return res[0]
```

### 207. Course Schedule

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if preMap[course] == []:
                return True
            visiting.add(course)

            for pre in preMap[course]:
                if not dfs(pre):
                    visiting.remove(course)
                    return False
            visiting.remove(course)
            preMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
```

### 79. Word Search

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False

            char = board[r][c]
            board[r][c] = "#"
            found = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1))
            board[r][c] = char
            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        return False
```

### 322. Coin Change

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1
```

### 146. LRU Cache

```python
from typing import Optional

class Node:
    __slots__ = ("key", "val", "prev", "next")

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: Node) -> None:
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def addFront(self, node: Node) -> None:
        first = self.head.next
        node.prev = self.head
        node.next = first
        self.head.next = node
        first.prev = node

    def moveToFront(self, node: Node) -> None:
        self.remove(node)
        self.addFront(node)

    def popLRU(self) -> Node:
        lru = self.tail.prev
        self.remove(lru)
        return lru

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node is None:
            return -1
        self.moveToFront(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node is not None:
            node.val = value
            self.moveToFront(node)
            return

        if len(self.cache) == self.cap:
            lru = self.popLRU()
            del self.cache[lru.key]

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.addFront(new_node)
```

### 239. Sliding Window Maximum

```python
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        l = 0

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if q[0] < l:
                q.popleft()
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
        return res
```

### 994. Rotting Oranges

```python
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh, time = 0, 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

            time += 1
        return time if fresh == 0 else -1
```

### 23. Merge k Sorted Lists

```python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.mergeTwoLists(l1, l2))
            lists = merged
        return lists[0]

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 or l2
        return dummy.next
```

### 347. Top K Frequent Elements

```python
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, c in counts.items():
            buckets[c].append(num)

        res = []
        for c in range(len(buckets) - 1, 0, -1):
            res.extend(buckets[c])
            if len(res) >= k:
                return res[:k]
```
