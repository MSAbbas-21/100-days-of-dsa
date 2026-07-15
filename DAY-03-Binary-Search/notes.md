# Binary Search (Medium) – First Occurrence of an Element

## What is this problem?

In a normal Binary Search, we stop as soon as we find the target.

But sometimes the array contains duplicate values, and we need to find the **first occurrence** of the target instead of just any occurrence.

---

## Example

Array:

[2, 5, 8, 8, 8, 12, 15, 20]

Target = 8

Output:

First occurrence is at index 2.

---

## How does it work?

- Start searching like a normal Binary Search.
- If the middle element is not the target, continue searching left or right based on the comparison.
- If the target is found:
  - Save its index.
  - Don't stop searching.
  - Move to the left half to check if the same value appears earlier.
- When the loop ends, the saved index will be the first occurrence.

---

## Why don't we stop after finding the target?

Because there might be another occurrence of the same value before the current one.

For example:

[2, 5, 8, 8, 8, 12]

If Binary Search finds the element at index 4, it doesn't mean it's the first one. We continue searching on the left to find the earliest position.

---

## Key Idea

The only difference from a normal Binary Search is:

- Store the current index when the target is found.
- Continue searching on the left side (`right = mid - 1`).

---

## Time Complexity

- Best Case: O(log n)
- Average Case: O(log n)
- Worst Case: O(log n)

## Space Complexity

- O(1)

---

## When is this useful?

- Finding the first record with a specific ID.
- Searching duplicate values in a sorted array.
- Database searches.
- Log and event analysis.

---

## Things to Remember

- The array must be sorted.
- Keep a variable (like `result`) to store the answer.
- Don't stop when you find the target.
- Continue searching on the left side.
- Return the stored index after the loop finishes.

---

## What I Learned

A small change in Binary Search can solve different types of problems. Instead of stopping after finding the target, I can keep searching to find the first or last occurrence. This idea is used in many interview questions.