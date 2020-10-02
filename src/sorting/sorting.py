# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    i=j=m=0
   
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[m] = arrA[i]
            i += 1
        else:
            merged_arr[m] = arrB[j]
            j += 1
        m += 1
    while i < len(arrA):
        merged_arr[m] = arrA[i]
        i += 1
        m += 1
    while j < len(arrB):
        merged_arr[m] = arrB[j]
        j += 1
        m += 1

    return merged_arr

arr1 = [1,4,7,9]
arr2 = [2,5,8,10,12,20,25]

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr): #O(nlog(n))
    if len(arr) <= 1:
        return arr
   
    left = merge_sort( arr[:len(arr) // 2] )
    right= merge_sort(arr[len(arr) // 2:])
    return merge(left, right)
    
arr10 = [4,6,9,7,5]
print(merge_sort(arr10))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input

def merge_in_place(arr, start, mid, end):
    left = arr[start:mid +1]
    right = arr[mid +1:end +1]
    i = j = 0
    m = start
    for index in range(m, end +1):
        if j >= len(right) or (i < len(left) and left[i] < right[j]):
            arr[index] = left[i]
            i +=1
        else:
            arr[index] = right[j]
            j +=1

def merge_sort_in_place(arr, l, r):
    if r - l > 0:
        middle = (l + r) // 2
        merge_sort_in_place(arr, l, middle)
        merge_sort_in_place(arr,middle+1,r)
        merge_in_place(arr,l,middle,r)

arr3 = [2,5,8,10,12,20,25]
arr10 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
merge_sort_in_place(arr10,0,len(arr10)-1)
print(arr10)

merge_sort_in_place(arr3,0,len(arr3)-1)
print(arr3)




# def merge_in_place(arr, start, mid, end):
#     left = arr[start:mid]
#     right = arr[mid:end]
#     i = j = 0
#     m = start
#     for index in range(m, end):
#         if j >= len(right) or (i < len(left) and left[i] < right[j]):
#             arr[index] = left[i]
#             i +=1
#         else:
#             arr[index] = right[j]
#             j +=1

# def merge_sort_in_place(arr, l, r):
#     if r - l > 1:
#         middle = (l + r) // 2
#         merge_sort_in_place(arr, l, middle)
#         merge_sort_in_place(arr,middle,r)
#         merge_in_place(arr,l,middle,r)

# arr111 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# merge_sort_in_place(arr111,0,len(arr111))
# print(arr111)

