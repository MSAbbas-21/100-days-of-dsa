# Day 1 Notes - Arrays & Big O

## What I understood today

* Arrays are used to store multiple values in one variable.
* In Python, we use **lists** instead of traditional arrays.
* Every element has an index.
* Indexing starts from **0**, not 1.
* Arrays make it easier to work with large amounts of data.

Example:

```python
arr = [10, 20, 30, 40]
```

---

## Traversing an Array

Traversal means visiting every element one by one.

There are two ways I learned:

```python
for num in arr:
    print(num)
```

and

```python
for i in range(len(arr)):
    print(arr[i])
```

### Difference

* `num` gives the actual value.
* `i` gives the index.
* If I need to change an element, using the index is usually more useful.

---

## Big O

Big O tells me how efficient my code is when the input size increases.

### O(1)

Accessing an element using its index.

```python
print(arr[2])
```

Very fast because Python directly knows where the element is.

---

### O(n)

Looping through the whole array.

```python
for num in arr:
    print(num)
```

If the array gets bigger, the loop also runs more times.

---

### O(n²)

Nested loops.

```python
for i in arr:
    for j in arr:
        print(i, j)
```

This becomes slow when the array is large.

---

## Largest Element

Idea:

* Assume the first element is the largest.
* Compare every other element.
* If I find a bigger one, update the variable.
* At the end, print the largest.

Time Complexity: **O(n)**

Space Complexity: **O(1)**

---

## Second Largest

This problem was harder than I expected.

What I learned:

* I need two variables:

  * `largest`
  * `second_largest`
* When I find a new largest value, the old largest becomes the second largest.
* I should ignore duplicate largest values.

---

## Mistakes I Made

* At first, I thought array indexing started from 1.
* I forgot that `for value in arr` doesn't let me modify the original list.
* I got confused between `value` and `index`.
* I couldn't solve the second largest problem without help.
* I need to practice dry running before writing code.

---

## Things to Remember

* Arrays (lists) keep the order of elements.
* Accessing an index is O(1).
* Traversing is O(n).
* Nested loops are often O(n²).
* Always think about edge cases before saying the code is correct.

Examples to test:

* One element
* Duplicate values
* Negative numbers
* Sorted array
* Reverse sorted array

---

## Interview Questions

* What is an array?
* Why is array indexing O(1)?
* Why is linear search O(n)?
* Difference between traversal and searching?
* Difference between `for value in arr` and `for i in range(len(arr))`?

---

## Today's Summary

Today I learned the basics of arrays and Big O notation. The largest element problem was easy after understanding traversal. The second largest problem was challenging because I had to keep track of two values at the same time. I need more practice with dry runs before coding.
