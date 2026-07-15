# Theory - Binary Search (First Occurrence)

Binary Search is an efficient searching algorithm that works only on **sorted arrays**. It repeatedly divides the search space into two halves until the target element is found or the search space becomes empty.

In the normal Binary Search algorithm, the search stops immediately when the target element is found. However, if the array contains duplicate elements, this does not guarantee that we have found the first occurrence.

To solve this problem, we modify the Binary Search algorithm slightly. Whenever the target is found, we store its index but continue searching in the left half of the array. This helps us check if the same element appears at an earlier position. After the search is completed, the stored index represents the first occurrence of the target.

This approach is much more efficient than using a linear search because it still performs the search in logarithmic time.

### Key Points

- Works only on a sorted array.
- Used when duplicate elements are present.
- Stores the index whenever the target is found.
- Continues searching on the left side to find the earliest occurrence.
- Returns the first occurrence after the search is completed.

### Time Complexity

- Best Case: **O(log n)**
- Average Case: **O(log n)**
- Worst Case: **O(log n)**

### Space Complexity

- **O(1)**