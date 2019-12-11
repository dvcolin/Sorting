# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
# 3. Start merging your single lists of one element together into larger, sorted sets
# 4. Repeat step 3 until the entire data set has been reassembled
    a_index = 0
    b_index = 0
    for i in range(elements):
         # if arrA is empty, add values from b
        if a_index >= len(arrA):
            merged_arr[i] = arrB[b_index]
            b_index += 1

        # if arrB is empty, add values from a
        elif b_index >= len(arrB):
            merged_arr[i] = arrA[a_index]
            a_index += 1

        # if value at arrA[a_index] is greater
        elif arrA[a_index] < arrB[b_index]:
            merged_arr[i] = arrA[a_index]
            a_index += 1

        # if value at arrB[b_index] is greater
        elif arrB[b_index] < arrA[a_index]:
            merged_arr[i] = arrB[b_index]
            b_index += 1
        else:
            merged_arr[i] = arrA[a_index]
            a_index += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # 1. While your data set contains more than one item, split it in half
    # 2. Once you have gotten down to a single element, you have also * sorted * that element
    # (a single element cannot be "out of order")
    if len(arr) > 1:
        halfpoint = len(arr) // 2

        arrA = arr[:halfpoint]
        arrB = arr[halfpoint:]

        arrA = merge_sort(arrA)
        arrB = merge_sort(arrB)

        arr = merge(arrA, arrB)
    return arr


print(merge_sort([5, 2, 7, 12, 3, 21, 15, 17, 15, 19, 4, 2]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
