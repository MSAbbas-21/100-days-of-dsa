# Bubble Sort Notes

## Definition

Bubble Sort is a simple comparison-based sorting algorithm that repeatedly compares two adjacent elements and swaps them if they are in the wrong order. After each pass, the largest unsorted element moves to its correct position at the end of the array.

---

## Why is it called Bubble Sort?

The largest element "bubbles up" to the end of the array after each pass, just like an air bubble rises to the surface of water.

---

## How Bubble Sort Works

1. Start from the first element.
2. Compare two adjacent elements.
3. Swap them if the left element is greater than the right element.
4. Continue until the end of the array.
5. Repeat the process until the array is sorted.

---

## Pseudocode

```
BubbleSort(Array)

n = length of Array

FOR i = 0 TO n - 2

    swapped = False

    FOR j = 0 TO n - i - 2

        IF Array[j] > Array[j + 1]

            Swap(Array[j], Array[j + 1])

            swapped = True

    END FOR

    IF swapped == False

        BREAK

END FOR

RETURN Array
```

---

## Example

Input

```
[11, 25, 9, 12, 5]
```

Pass 1

```
[11, 9, 12, 5, 25]
```

Pass 2

```
[9, 11, 5, 12, 25]
```

Pass 3

```
[9, 5, 11, 12, 25]
```

Pass 4

```
[5, 9, 11, 12, 25]
```

Output

```
[5, 9, 11, 12, 25]
```

---

## Time Complexity

| Case                  | Complexity |
| --------------------- | ---------- |
| Best Case (Optimized) | O(n)       |
| Average Case          | O(n²)      |
| Worst Case            | O(n²)      |

---

## Space Complexity

```
O(1)
```

---

## Properties

* In-place Sorting: Yes
* Stable Sorting: Yes
* Comparison-based: Yes
* Adaptive: Yes (Optimized version)

---

## Advantages

* Easy to understand.
* Easy to implement.
* Good for learning sorting algorithms.
* Uses very little extra memory.

---

## Disadvantages

* Slow for large datasets.
* Performs many comparisons.
* Rarely used in production systems.

---

## Interview Questions

1. What is Bubble Sort?
2. Why is it called Bubble Sort?
3. How does Bubble Sort work?
4. What is the time complexity of Bubble Sort?
5. What is the space complexity?
6. Is Bubble Sort stable?
7. Is Bubble Sort an in-place algorithm?
8. Why do we use `range(n - i - 1)`?
9. What is the purpose of the `swapped` variable?
10. When should Bubble Sort not be used?

---

## Important Points to Remember

* Compare adjacent elements.
* Swap if the left element is greater.
* After every pass, the largest element reaches its correct position.
* The optimized version stops early if no swaps occur during a pass.
* Bubble Sort is mainly used for learning and interview preparation.

---

## Revision (30 Seconds)

* Compare adjacent elements.
* Swap if needed.
* Largest element moves to the end after each pass.
* Best: O(n)
* Average: O(n²)
* Worst: O(n²)
* Space: O(1)
* Stable: Yes
* In-place: Yes
* Optimization: Use `swapped` to stop early.
