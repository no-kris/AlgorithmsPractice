# Problem 6: The Seasonal Price Trend

---

### 📖 Background
> You are analyzing the price of a seasonal item over several years. A "Peak Season" is a continuous period where the price strictly increases to a maximum and then strictly decreases. You need to identify the longest such "Peak Season" to understand customer demand cycles.

### 📝 Problem Definition
Given an array `prices`, find the length of the longest contiguous subarray that is "bitonic" (strictly increasing then strictly decreasing). A subarray of length 1 or 2 is considered bitonic.

### 💡 Examples

**Example 1:**
```text
Input:  prices = [1, 2, 3, 2, 1]
Output: 5
Explanation: The whole array is bitonic.
```

**Example 2:**
```text
Input:  prices = [1, 2, 3, 4, 5]
Output: 5
Explanation: Strictly increasing is a subset of bitonic.
```

**Example 3:**
```text
Input:  prices = [1, 2, 1, 2, 3, 2]
Output: 4
Explanation: [1, 2, 3, 2] is the longest bitonic subarray.
```

---

### ⚙️ Constraints
- `1 <= array.length <= 10^5`

### 📤 Expected Output
An **integer** representing the length of the longest bitonic subarray.