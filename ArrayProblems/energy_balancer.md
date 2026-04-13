# Problem 9: The Energy Grid Load Balancer

---

### 📖 Background
> A smart power grid has multiple energy sources. To maintain stability, the combined power output of any window of `k` consecutive sources must not exceed a specific `limit`. You are tasked with determining if the current grid configuration is stable.

### 📝 Problem Definition
Given an array `power_outputs` and integers `k` and `limit`, return `true` if the sum of every contiguous window of size `k` is less than or equal to `limit`, and `false` otherwise.

### 💡 Examples

**Example 1:**
```text
Input:  power_outputs = [1, 2, 3, 4], k = 2, limit = 5
Output: false
Explanation: [2, 3] = 5 (ok), [3, 4] = 7 (too high).
```

**Example 2:**
```text
Input:  power_outputs = [1, 2, 3, 4], k = 2, limit = 7
Output: true
Explanation: All windows [1,2]=3, [2,3]=5, [3,4]=7 are <= 7.
```

**Example 3:**
```text
Input:  power_outputs = [5, 5, 5], k = 1, limit = 4
Output: false
Explanation: [5] > 4.
```

---

### ⚙️ Constraints
- `1 <= array.length <= 10^5`
- `1 <= k <= array.length`

### 📤 Expected Output
A **boolean** value (`true` or `false`).