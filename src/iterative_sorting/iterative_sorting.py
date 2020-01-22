# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        while cur_index < len(arr):
            if arr[cur_index] < arr[smallest_index]:
                smallest_index = cur_index
            cur_index += 1

        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swaps = True
    while swaps == True:
        swaps = False
        cur_index = 0
        # While cur_index is less than last index, set next_index to cur_index + 1
        while cur_index < len(arr) - 1:
            next_index = cur_index + 1
            # If number at current index is greater than next number, swap them and cur_index = 0
            if arr[cur_index] > arr[next_index]:
                arr[cur_index], arr[next_index] = arr[next_index], arr[cur_index]
                swaps = True
            # Increase current index by 1
            cur_index += 1
    return arr


# # STRETCH: implement the Count Sort function below
# def count_sort(arr, maximum=-1):

#     return arr
