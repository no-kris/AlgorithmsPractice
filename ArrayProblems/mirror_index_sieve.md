# Problem 2: The Warehouse Inventory Balance

---

### 📖 Background
> You are managing a regional warehouse inventory. Items are stored in a long line of shelves. A "Balanced Point" is an inventory shelf where the total count of items on all shelves to the left is exactly equal to the total item count on all shelves to the right. You need to identify all such shelves for efficient inventory auditing.

### 📝 Problem Definition
Given an array `shelves`, find all indices `i` where:
`sum(shelves[0...i-1]) == sum(shelves[i+1...n-1])`
*(If a side is empty, the sum is 0).*

### 💡 Examples

**Example 1:**
```text
Input:  shelves = [1, 2, 3, 4, 6]
Output: [3]
Explanation: i=3. Left sum: 1+2+3 = 6. 
             Right sum: shelves[4] = 6.
             6 == 6. Match!
```

**Example 2:**
```text
Input:  shelves = [1, 1, 1, 1]
Output: []
Explanation: No index satisfies the condition.
```

**Example 3:**
```text
Input:  shelves = [2, 5, 2]
Output: [1]
Explanation: i=1. Left sum: shelves[0] = 2. 
             Right sum: shelves[2] = 2.
             2 == 2. Match!
```

---

### ⚙️ Constraints
- `1 <= array.length <= 10^4`
- `1 <= array[i] <= 100`

### 📤 Expected Output
A **sorted array** of indices where the condition holds.