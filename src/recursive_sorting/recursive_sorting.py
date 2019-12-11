# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
# 3. Start merging your single lists of one element together into larger, sorted sets
# 4. Repeat step 3 until the entire data set has been reassembled
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # 1. While your data set contains more than one item, split it in half
    # 2. Once you have gotten down to a single element, you have also * sorted * that element
    # (a single element cannot be "out of order")
    left_array = arr[:len(arr) // 2]
    if len(arr) >= 2:
        right_array = arr[len(arr) // 2: len(arr)]

    print(left_array)
    print(right_array)
    while len(arr) > 1:
        merge_sort(left_array)
        merge_sort(right_array)
        return arr
    return arr


merge_sort([5, 2, 7, 12, 73, 21, 4, 18])


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
