import array
arr = array.array('i', [99, 98, 97, 96, 95])
def display():
	for n in arr:
    	print(n, end = "\t" )

print("Before:")
display()

for i in range (0,5):
	min = arr[i]
	j = i - 1
	while j >= 0 and min < arr[j]:
    	arr[j+1] = arr[j]
    	j = j - 1
	arr[j + 1] = min

print("\nAfter:")
display()
