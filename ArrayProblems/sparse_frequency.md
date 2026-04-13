# Problem 3: The Prime-Occurence Telemetry Logger

---

### 📖 Background
> You are managing telemetry data from a planetary rover. The rover sends millions of pings, many redundant. To minimize data transmission costs, you are tasked with creating a "Selective Summary": a report containing only those sensor identifiers that have appeared a *prime* number of times.

### 📝 Problem Definition
Given a massive array of integers, output a report structure (e.g., a dictionary, map, or custom struct) that maps the integer value to its frequency, but only for those values whose total count is a prime number.

### 💡 Examples

**Example 1:**
```text
Input:  pings = [10, 20, 10, 30, 10, 20, 30, 30, 30]
Output: {10: 3, 20: 2}
Explanation: 3 and 2 are prime. 4 (count of 30) is not.
```

**Example 2:**
```text
Input:  pings = [5, 5, 5, 5, 5]
Output: {5: 5}
Explanation: 5 is prime.
```

**Example 3:**
```text
Input:  pings = [1, 2, 3, 4]
Output: {}
Explanation: No counts are prime (1 is not prime).
```

---

### ⚙️ Constraints
- `1 <= array.length <= 10^7`
- `1 <= array[i] <= 10^6`

### 📤 Expected Output
A **mapping** of `{value: frequency}`.