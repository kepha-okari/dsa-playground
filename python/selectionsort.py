# Recursive function to perform selection sort on sublist `A[i…n]`
def selectionSort(arr):

    n = len(arr)

    for i in range(n):

        index_of_min = i #initialize track index of the minimum value

        for j in range(i+1, n): #iterate through the unsorted part

            if arr[j] < arr[i]:

                index_of_min = j #mark the index of the current minimum value in the unsorted part of array

        arr[i], arr[index_of_min] = arr[index_of_min], arr[i]

    return arr
        

if __name__ == '__main__':

	A = [3, 8, 5, 4, 1, 9, -2]
	print(selectionSort(A))

