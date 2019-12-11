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
    def sort_loop():
        cur_index = 0
        swaps = 0
        # Loop through your array
        while cur_index < len(arr) - 1:
            next_index = cur_index + 1
# Compare each element to its neighbor
            if arr[cur_index] > arr[next_index]:
                # If elements in wrong position (relative to each other, swap them)
                arr[cur_index], arr[next_index] = arr[next_index], arr[cur_index]
                swaps += 1
            cur_index += 1
# If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
        if swaps != 0:
            sort_loop()
    sort_loop()
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
