list = list(map(int,input("Enter List: ").split()))
def min_max(low, high):
    print(list[low:high+1])
    if low == high:
        return list[low], list[low]
    elif low == high-1:
        if list[low] < list[high]:
            return list[low], list[high]
        else:
            return list[high], list[high]
    else:
        mid = int((low+high)/2)
        l_min, l_max = min_max(low, mid)
        r_min, r_max = min_max(mid, high)
        minimum = l_min if l_min < r_min else r_min
        maximum = l_max if l_max > r_max else r_max
        return minimum, maximum
print(list)
minimum, maximum = min_max(0,len(list)-1)
print(f"Minimum: {minimum}\nMaximum: {maximum}")
