def qsort(arr):
    if len(arr) <= 1:
            return arr
    else:
        return qsort([x for x in arr[1:] if x < arr[0]]) + \
               [arr[0]] + \
               qsort([x for x in arr[1:] if x >= arr[0]])


arr=[5,1,5,3,2,6,7,12,3,35,6]
print(qsort(arr))
