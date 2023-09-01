# Recursive function to perform quick sort on sublist `A[i…n]`
def quickSort(arr):

    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2] # pivot value/ middle value
    print(pivot)

    left = [x for x in arr if x < pivot] # elements left of pivot
    middle = [x for x in arr if x == pivot] # elements equal to pivot
    right = [x for x in arr if x > pivot] # element right of pivot

    # recursively sort the subarrays and merge them
    return quickSort(left) + middle + quickSort(right)

if __name__ == '__main__':

	A = [3, 8, 5, 4, 1, 9, -2]
	print(quickSort(A))

