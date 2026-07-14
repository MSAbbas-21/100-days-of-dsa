# 📘 Linear Search - Medium

## Definition
Linear Search is a searching algorithm that checks each element of an array one by one until the target element is found or the array ends.

---

# Problem Statement

Given an array and a target element:

- Print the index of the target if it exists.
- Otherwise, print `"Not Found"`.

---

# Algorithm

1. Store the array.
2. Store the target element.
3. Traverse the array from the first index to the last.
4. Compare the current element with the target.
5. If both are equal:
   - Print the current index.
   - Stop the loop.
6. If the loop completes without finding the target:
   - Print `"Not Found"`.

---

# Pseudocode

```
START

Input array
Input target

FOR each index in the array

    IF current element == target

        Print index
        Stop the loop

IF target is not found

    Print "Not Found"

END
```

---

# Syntax

```python
for i in range(len(arr)):
    if arr[i] == target:
        print("Found at index", i)
        break
else:
    print("Not Found")
```

---

# Example

### Input

```python
arr = [10, 20, 30, 40, 50]
target = 40
```

### Output

```
Found at index 3
```

---

# Dry Run

| Index | Element | Target | Result |
|-------:|--------:|-------:|--------|
| 0 | 10 | 40 | ❌ |
| 1 | 20 | 40 | ❌ |
| 2 | 30 | 40 | ❌ |
| 3 | 40 | 40 | ✅ Found |
| 4 | - | - | Loop Stops |

---

# Explanation

## `len(arr)`

Returns the total number of elements.

```python
len(arr)
```

Output

```
5
```

---

## `range(len(arr))`

Returns all valid indexes.

```python
range(len(arr))
```

Output

```
0, 1, 2, 3, 4
```

---

## `arr[i]`

Accesses the element at index `i`.

Example:

```python
arr = [10, 20, 30]
```

| i | arr[i] |
|---|--------|
| 0 | 10 |
| 1 | 20 |
| 2 | 30 |

---

## `break`

Stops the loop immediately after finding the target.

---

## `for...else`

The `else` block executes only if the loop completes without `break`.

---

# Time Complexity

| Case | Complexity |
|------|------------|
| Best Case | O(1) |
| Average Case | O(n) |
| Worst Case | O(n) |

---

# Space Complexity

```
O(1)
```

---

# Advantages

- Easy to understand.
- Easy to implement.
- Works on both sorted and unsorted arrays.
- No extra memory required.

---

# Disadvantages

- Slow for large datasets.
- Checks elements one by one.
- Less efficient than Binary Search.

---

# Interview Questions

### 1. What is Linear Search?

Linear Search is a searching algorithm that checks each element one by one until the target is found.

---

### 2. Why use `range(len(arr))`?

To get the index of each element.

---

### 3. Why use `arr[i]`?

To access the current element using its index.

---

### 4. Why use `break`?

To stop searching after finding the target.

---

### 5. When does the `else` block execute?

When the loop completes without executing `break`.

---

# Key Points

- Linear Search checks elements sequentially.
- Works on sorted and unsorted arrays.
- `range(len(arr))` gives indexes.
- `arr[i]` accesses elements.
- `break` stops the loop.
- `for...else` handles the "Not Found" case.
- Best Case → **O(1)**
- Worst Case → **O(n)**
- Space Complexity → **O(1)**