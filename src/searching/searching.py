# TO-DO: Implement a recursive implementation of binary search
#the worst case is O(n), the average case is log(n)
def binary_search(arr, target, start, end):
    middle = (start + end) // 2
    if start > end:
        return -1
    if arr[middle] == target:
        return middle
    if arr[middle] > target:
        return binary_search(arr, target, start, (middle -1) )
    else:
        return binary_search(arr, target,  (middle + 1), end)

# arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
# asc1 = [2, 4, 12, 14, 17, 30, 46, 47, 51, 54, 61]
# print(binary_search(asc1, 12, 0, len(asc1) - 1))
# print(binary_search(arr1, 9, 0, len(arr1) - 1))

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively

def agnostic_binary_search(arr, target):
    ascending = 0
    if arr[0] < arr[len(arr)-1]:
        ascending = 1 
    start = 0
    end = len(arr) - 1
    found = -1

    while start <= end and found < 0:
        middle = (start + end) // 2
        if arr[middle] == target:
            found = middle
            return found
        if ascending == 1:
            if arr[middle] > target:
                end = middle -1
            if arr[middle] < target: 
                start = middle +1
        else:
            if arr[middle] > target:
                start = middle +1
            if arr[middle] < target: 
                end = middle -1

    return found 

#----------------recursively-------------------------
def agnostic_binary_search1(arr, target,start, end):
    
    ascending = 0
    if arr[0] < arr[len(arr)-1]:
        ascending = 1 
    middle = (start + end) // 2
    if start > end:
        return -1
    if arr[middle] == target:
        return middle

    if ascending == 1:
        if arr[middle] > target:
            return agnostic_binary_search1(arr, target, start, middle-1)
        else:
            return agnostic_binary_search1(arr, target,middle+1, end)
    else:
        if arr[middle] > target:
            return agnostic_binary_search1(arr, target, middle +1, end)
        else:
            return agnostic_binary_search1(arr, target, start, middle-1)

ascending = [2, 4, 12, 14, 17, 30, 46, 47, 51, 54, 61]
descending = [101, 98, 57, 49, 45, 13, -3, -17, -61]
print(agnostic_binary_search1(ascending, 12, 0, len(ascending) - 1))
print(agnostic_binary_search1(descending, 49, 0, len(descending) - 1))
    


    
    
    

