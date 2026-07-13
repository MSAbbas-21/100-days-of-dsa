arr = [10, 5, 18, 22, 7]

largest = float("-inf")
second_largest = float("-inf")

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

if second_largest == float("-inf"):
    print("No second largest element found.")
else:
    print("Second largest element:", second_largest)