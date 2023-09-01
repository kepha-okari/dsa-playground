# Recursive function to perform bubble sort on sublist `A[i…n]`
def bubbleSort(arr):

    n = len(arr)

    for i in range(n): # outer

        swapped = False

        for j in range(n - i - 1): #last i elements are already sorted and well positioned

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j] #swap 

                swapped = True

        if not swapped:
            break                   

    return arr
        

if __name__ == '__main__':

	A = [3, 8, 5, 4, 1, 9, -2]
	print(bubbleSort(A))

