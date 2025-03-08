arr = [5, 1, 4, 3, 2]
for i in range(0, 5):
    low = i
    for j in range(i+1, 5):
        if arr[j] < arr[low]:
            low = j
    arr[i], arr[low] = arr[low], arr[i]
print(arr)
