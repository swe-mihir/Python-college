element = list(map(int, input("Enter the elements: ").split(" ")))
wt = list(map(int, input("Enter the respective weights: ").split(" ")))
value = list(map(int, input("Enter the respective values: ").split(" ")))
capacity = int(input("Enter the capacity: "))
n = len(element)
weight = 0
profit = 0
ratio = []
sequence = []
for i in range(0, n):
    sequence.append(0)
    ratio.append(value[i]/wt[i])

for j in range(0, n-1):
    for i in range(0, n-1):
        if ratio[i]  < ratio[i+1]:
            ratio[i], ratio[i+1] = ratio[i+1], ratio[i]
            element[i],element[i+1] = element[i+1],element[i]
            value[i],value[i+1] = value[i+1],value[i]
            wt[i],wt[i+1] = wt[i+1],wt[i]
for i in range(0,n-1):
    if weight+wt[i] <= capacity:
        sequence[i] = 1
        weight = weight + wt[i]
        profit += value[i]
    else:
        fraction = round((capacity-weight)/wt[i], 2)
        sequence[i] = fraction
        profit += value[i] * fraction
        weight = capacity

print("Elements: ", element)
print("Fraction: ", sequence)
print("Profit: ", profit)
