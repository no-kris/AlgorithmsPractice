# Problem 10: The Inventory Shortfall Finder

---

### 📖 Background
> You are scanning a list of product IDs. Sometimes, a batch of items is mislabeled or lost, creating a gap in the sequence. You need to identify the first missing product ID in the sequence.

### 📝 Problem Definition
Given a sorted array of distinct integers, find the smallest non-negative integer that is not present in the array.

### 💡 Examples

**Example 1:**
```text
Input:  ids = [0, 1, 2, 4, 5]
Output: 3
```

**Example 2:**
```text
Input:  ids = [1, 2, 3]
Output: 0
```

**Example 3:**
```text
Input:  ids = [0, 1, 2, 3, 5]
Output: 4
```

---

### ⚙️ Constraints
- `1 <= array.length <= 10^5`

### 📤 Expected Output
An **integer** representing the smallest missing non-negative ID.
