# Problem 7: The Document Clusterer

---

### 📖 Background
> You are processing a stream of incoming documents, each tagged with a category ID. You want to group these documents into "clusters" by removing all documents that don't belong to a repeating sequence of a specific category.

### 📝 Problem Definition
Given an array `categories`, find the length of the longest subarray where each element appears at least twice in that subarray.

### 💡 Examples

**Example 1:**
```text
Input:  categories = [1, 2, 1, 3, 2, 3]
Output: 6
Explanation: The whole array works.
```

**Example 2:**
```text
Input:  categories = [1, 1, 2, 2, 3]
Output: 4
Explanation: [1, 1, 2, 2] is the longest.
```

**Example 3:**
```text
Input:  categories = [1, 2, 3, 4]
Output: 0
Explanation: No element appears twice.
```

---

### ⚙️ Constraints
- `1 <= array.length <= 10^5`

### 📤 Expected Output
An **integer** representing the length of the longest valid subarray.