# Problem 4: The Sub-grid Shifter

---

### 📖 Background
> You are building an image processing filter for an old-school arcade monitor. The image is stored as a linear array of pixel intensities. A processing effect requires that every window of size `p` undergoes a specific cyclic shift `r` to create a "glitch" effect.

### 📝 Problem Definition
Partition the array `pixels` into windows of length `p`. For each full window, shift all elements `r` positions to the right within that window. If the remaining elements at the end form a window smaller than `p`, they must remain untouched. This must be done in-place to save memory on the device's hardware.

### 💡 Examples

**Example 1:**
```text
Input:  pixels = [1, 2, 3, 4, 5, 6, 7], p = 3, r = 1
Output: [3, 1, 2, 6, 4, 5, 7]
```

**Example 2:**
```text
Input:  pixels = [1, 2, 3, 4, 5, 6, 7], p = 2, r = 2
Output: [1, 2, 3, 4, 5, 6, 7]
```

**Example 3:**
```text
Input:  pixels = [1, 2, 3, 4, 5], p = 5, r = 2
Output: [4, 5, 1, 2, 3]
```

---

### ⚙️ Constraints
- `1 <= p <= array.length`
- `0 <= r <= p`

### 📤 Expected Output
The modified array (in-place).