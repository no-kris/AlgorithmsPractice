# Problem 8: The Meeting Room Optimizer

---

### 📖 Background
> You have a series of meetings scheduled for the day, each with a start and end time. You want to find the maximum number of meetings that can be scheduled in a single room without any overlaps.

### 📝 Problem Definition
Given an array of pairs `[start, end]`, return the maximum number of non-overlapping meetings you can attend.

### 💡 Examples

**Example 1:**
```text
Input:  meetings = [[1, 2], [2, 3], [3, 4]]
Output: 3
Explanation: You can attend all three.
```

**Example 2:**
```text
Input:  meetings = [[1, 3], [2, 4], [3, 5]]
Output: 2
Explanation: You can attend [1, 3] and [3, 5].
```

**Example 3:**
```text
Input:  meetings = [[1, 5], [2, 3], [4, 6]]
Output: 2
Explanation: You can attend [2, 3] and [4, 6].
```

---

### ⚙️ Constraints
- `1 <= array.length <= 10^4`

### 📤 Expected Output
An **integer** representing the maximum number of meetings.