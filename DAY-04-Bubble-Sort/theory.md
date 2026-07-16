# Bubble Sort - Theory

## Definition

Bubble Sort is a simple comparison-based sorting algorithm that repeatedly compares adjacent elements and swaps them if they are in the wrong order. After each pass, the largest unsorted element moves to its correct position at the end of the array.

## Working Principle

* Compare two adjacent elements.
* Swap them if the left element is greater than the right element.
* Continue until the end of the array.
* Repeat the process until the array is completely sorted.

## Why is it called Bubble Sort?

It is called Bubble Sort because the largest element "bubbles up" to the end of the array after each pass.

## Time Complexity

* Best Case: **O(n)** (Optimized Bubble Sort)
* Average Case: **O(n²)**
* Worst Case: **O(n²)**

## Space Complexity

* **O(1)** (In-place sorting)

## Advantages

* Easy to understand and implement.
* Requires constant extra memory.
* Suitable for small datasets and learning.

## Disadvantages

* Inefficient for large datasets.
* Performs many unnecessary comparisons.
* Slower than Merge Sort and Quick Sort.

## Key Points

* Compares adjacent elements.
* Swaps elements when needed.
* Largest element reaches its correct position after each pass.
* Uses nested loops.
* Can be optimized using a `swapped` flag.

## Interview Keywords

* Comparison-based Sorting
* Stable Sorting Algorithm
* In-place Sorting Algorithm
* Adaptive (Optimized Version)
