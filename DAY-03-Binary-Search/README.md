# Day 03 - Binary Search

## Overview

Today's topic is **Binary Search**, one of the most efficient searching algorithms. Unlike Linear Search, Binary Search works by repeatedly dividing the search space into two halves, making it much faster for large datasets.

**Note:** Binary Search works only on **sorted arrays**.

---

## Problems Solved

### Easy - Binary Search

**Problem:**  
Find the index of a target element in a sorted array.

**Example**

```python
arr = [2, 5, 8, 12, 15, 20, 25]
target = 15

Output:
Found at index 4
```

**Concepts Used**
- Sorted Array
- Two Pointers (`left` and `right`)
- Middle Element Calculation
- While Loop
- Conditional Statements

**Time Complexity:** `O(log n)`  
**Space Complexity:** `O(1)`

---

### Medium - First Occurrence of an Element

**Problem:**  
Find the **first occurrence** of a target element in a sorted array containing duplicate values.

**Example**

```python
arr = [2, 5, 8, 8, 8, 12, 15, 20]
target = 8

Output:
First occurrence found at index 2
```

### How It Works

- Perform Binary Search as usual.
- If the target is found:
  - Save the current index.
  - Continue searching on the left side.
- After the search ends, the stored index is the first occurrence.

**Time Complexity:** `O(log n)`  
**Space Complexity:** `O(1)`

---

## What I Learned

- Binary Search is much faster than Linear Search for sorted arrays.
- The search space is reduced by half in every iteration.
- Small changes to the Binary Search logic can solve different problems.
- Continuing the search after finding the target helps find the first occurrence.
- Understanding Binary Search opens the door to solving many interview questions.

---

## Folder Structure

```
DAY-03-Binary_Search/
│── easy.py
│── medium.py
└── README.md
```

---

## Key Takeaways

- Binary Search requires a sorted array.
- Always calculate the middle index carefully.
- Update `left` and `right` correctly to avoid infinite loops.
- The same algorithm can be modified to solve problems like:
  - First Occurrence
  - Last Occurrence
  - Count Occurrences
  - Search Insert Position
  - Peak Element
  - Search in Rotated Sorted Array

---

## Next Topic

➡️ **Day 04 - Bubble Sort**