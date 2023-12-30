def binary_search(l,val):
    start = 0
    end = len(l) - 1
    while start <= end:
        mid = (start + end) // 2
        if l[mid] < val:
            start = mid + 1
        elif l[mid] > val:
            end = mid - 1
        elif l[mid] == val:
            return start, mid, end
    return False
li = [100,322,343,456,500,601,802]
print(binary_search(li, 601))