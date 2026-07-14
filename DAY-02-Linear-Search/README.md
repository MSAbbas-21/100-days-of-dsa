# Day 1 - Linear Search (Medium)

## 📌 Problem

Given an array and a target element, find the index of the target using **Linear Search**.

If the target is found, print its index; otherwise, print **"Not Found"**.

---

## 📖 Theory

Linear Search is a searching algorithm that checks each element one by one until the target is found or the array ends.

**Also Known As:** Sequential Search

---

## 📝 Algorithm

1. Start from the first element.
2. Compare the current element with the target.
3. If they match, print the index and stop.
4. Otherwise, move to the next element.
5. If the loop finishes without finding the target, print `"Not Found"`.

---

## 💻 Code

```python
arr = [10, 20, 30, 40, 50]
target = 40

for i in range(len(arr)):
    if arr[i] == target:
        print("Found at index", i)
        break
else:
    print("Not Found")
```

---

## ▶️ Example

**Input**

```python
arr = [10, 20, 30, 40, 50]
target = 40
```

**Output**

```
Found at index 3
```

---

## ⏱️ Complexity

| Type | Complexity |
|------|------------|
| Best Case | O(1) |
| Average Case | O(n) |
| Worst Case | O(n) |
| Space Complexity | O(1) |

---

## ✅ Key Points

- Checks elements sequentially.
- Works on sorted and unsorted arrays.
- Uses `break` to stop when the target is found.
- `for...else` handles the "Not Found" case.
- Easy to implement but not efficient for large datasets.

---

## 📚 Concepts Practiced

- `for` loop
- `range(len())`
- Array indexing
- `if` statement
- `break`
- `for...else`
- Time Complexity
- Space Complexity