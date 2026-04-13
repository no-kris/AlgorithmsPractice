# Problem 5: The Terrain Smoother

---

### 📖 Background
> You are designing a terrain generation algorithm for a procedurally generated open-world game. The "natural" look of hills and valleys is defined by strict alternation: every high point must be surrounded by lower points, and every low point must be surrounded by higher points. You have an initial heightmap that contains irregularities; you need to remove the minimum number of data points to achieve this "Valley-Peak" property.

### 📝 Problem Definition
An array is a "Valley-Peak" if for every index `i` (from `1` to `n-2`), it satisfies:
`(arr[i-1] > arr[i] < arr[i+1])` (Valley)
OR
`(arr[i-1] < arr[i] > arr[i+1])` (Peak)
Find the minimum number of elements that must be removed so that the remaining sequence forms a valid Valley-Peak structure.

### 💡 Examples

**Example 1:**
```text
Input:  heightmap = [1, 2, 3, 2, 1]
Output: 2
Explanation: Remove '2' and '2'. Remaining: [1, 3, 1] (Peak).
```

**Example 2:**
```text
Input:  heightmap = [1, 2, 3, 4, 5]
Output: 3
Explanation: Remove '2, 3, 4'. Remaining: [1, 5] (or similar).
```

**Example 3:**
```text
Input:  heightmap = [10, 5, 10, 5, 10]
Output: 0
Explanation: Already alternates.
```

---

### ⚙️ Constraints
- `3 <= array.length <= 10^3`

### 📤 Expected Output
An **integer** representing the minimum number of removals.