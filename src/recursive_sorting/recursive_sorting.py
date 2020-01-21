# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    a_index = 0
    b_index = 0

    for i in range(elements):
        # If there are no more elements in arrA, add element from arrB and b_index += 1
        if a_index >= len(arrA):
            merged_arr[i] = arrB[b_index]
            b_index += 1
        # If there are no more elements in arrB, add element from arrA and a_index += 1
        elif b_index >= len(arrB):
            merged_arr[i] = arrA[a_index]
            a_index += 1
        # If element in arrA is smaller, add element to merged array, a_index += 1
        elif arrA[a_index] < arrB[b_index]:
            merged_arr[i] = arrA[a_index]
            a_index += 1
        # If element in arrB is smaller, add element to merged array, b_index += 1
        elif arrB[b_index] < arrA[a_index]:
            merged_arr[i] = arrB[b_index]
            b_index += 1
        # If numbers are equal, add element from arrA and a_index += 1
        else:
            merged_arr[i] = arrA[a_index]
            a_index += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    mid_index = len(arr) // 2
    arrA = arr[:mid_index]
    arrB = arr[mid_index:]
    if len(arr) > 1:
        arrA = merge_sort(arrA)
        arrB = merge_sort(arrB)

    sorted_arr = merge(arrA, arrB)
    return sorted_arr


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
