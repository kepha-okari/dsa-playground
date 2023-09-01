# Recursive function to perform insertion sort on sublist `A[i…n]`
def insertionSort(arr):

    n = len(arr)

    for i in range(1,n):

        current_smallest = arr[i] # assumed to be the smallest value

        j = i - 1 # init previous element

        while j >= 0 and arr[j] > current_smallest:
             
             arr[j+1], arr[j]  =  arr[j], current_smallest

             j -= 1
            
    return arr




if __name__ == '__main__':

	A = [3, 8, 5, 4, 1, 9, -2]
	print(insertionSort(A))

