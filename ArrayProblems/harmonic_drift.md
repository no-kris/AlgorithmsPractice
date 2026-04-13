# Problem 1: The Sensor Drift Calibration

---

### 📖 Background
> You are designing software for a deep-sea seismic sensor that reports readings over time. Due to electrical interference in the cabling, the sensor occasionally experiences "harmonic interference" where readings jump by exactly `k` units at each interval. You need to identify the longest period of continuous, clean data where this interference pattern holds true, as this is the only data that can be reliably recalibrated.

### 📝 Problem Definition
Given an array `drift_readings`, a "Harmonic Interval" is defined as a contiguous subarray of at least length 2, where the absolute difference between every pair of adjacent elements is exactly `k`. Find the length of the longest Harmonic Interval. If no such interval exists, return 0.

### 💡 Examples

**Example 1:**
```text
Input:  drift_readings = [10, 15, 20, 25, 30, 12, 14, 16], k = 5
Output: 5
Explanation: Subarray [10, 15, 20, 25, 30] has length 5.
```

**Example 2:**
```text
Input:  drift_readings = [1, 1, 1, 1], k = 0
Output: 4
Explanation: The difference between adjacent elements is consistently 0.
```

**Example 3:**
```text
Input:  drift_readings = [10, 20, 30, 40], k = 15
Output: 0
Explanation: No two adjacent elements have an absolute difference of 15.
```

---

### ⚙️ Constraints
- `1 <= array.length <= 10^5`
- `0 <= array[i] <= 10^9`
- `0 <= k <= 10^9`

### 📤 Expected Output
An **integer** representing the length of the longest subarray.
