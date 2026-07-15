arr = [2, 5, 8, 8, 8, 12, 15, 20]
target = 8

left = 0
right = len(arr) - 1
result = -1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
        result = mid
        right = mid - 1      # Continue searching on the left

    elif arr[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

if result != -1:
    print("First occurrence found at index", result)
else:
    print("Not Found")