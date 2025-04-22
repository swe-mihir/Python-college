item = list(map(int, input("Enter the items: ").split(" ")))
weight = list(map(int, input("Enter the weights: ").split(" ")))
value = list(map(int, input("Enter the values: ").split(" ")))

rows = len(item)
capacity = int(input("Enter capacity: "))
table = [[0 for i in range(capacity+1)] for j in range(rows+1)]

def display():
    for rows in table:
        print(rows)
        
for i in range(1,rows+1):
    for j in range(1, capacity+1):
        diff = j - weight[i-1]
        if diff >= 0:
            table[i][j] = max(table[i-1][j], table[i-1][diff]+value[i-1])
        else:
            table[i][j] = table[i-1][j]        
            
print("Final table: ")
display()
sequence = [0 for _ in range(rows)]

w = capacity

for i in range(rows, 0, -1):
    if table[i][w] != table[i-1][w]:
        sequence[i-1] = 1
        w -= weight[i-1]

print("Maximum value in knapsack:", table[rows][capacity])
print("Sequence: ", sequence)
