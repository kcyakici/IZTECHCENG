def binarySearch(arr, l, r, x):
    if l > r:
        return -1
    else:
        mid = l + (r-l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid+1, r, x)

