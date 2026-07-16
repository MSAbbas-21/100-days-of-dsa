mylist = [11, 25, 9, 12, 5]

n = len(mylist)

for i in range(n - 1):
    swapped = False

    for j in range(n - i - 1):
        if mylist[j] > mylist[j + 1]:
            mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
            swapped = True

    print(f"Pass {i + 1}: {mylist}")

    if not swapped:
        break

print("Sorted List:", mylist)