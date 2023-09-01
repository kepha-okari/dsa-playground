'''
    LINK : https://www.techiedelight.com/shrink-array-by-removing-triplets/

    Given an integer array, shrink it by removing adjacent triplets that satisfy the given constraints and return the total number of elements in the resultant array.

    A triplet (x, y, z) can only be removed if, for a given number k, the second element y of the triplet is precise k more than the first element x. The third element, z, is precise k more than the second element y. The total number of elements in the final array should be as few as possible.

    
    For example,

        Input:  A[] = [1, 2, 3, 5, 7, 8], k = 2
        
        Output: 3
        
        The adjacent triplet (3, 5, 7) can be removed from the array. The resultant array is [1, 2, 8] cannot be reduced further.
        
    
        Input:  A[] = [ ], k = 1
        
        Output: 0
    
        The result is 0 since we can remove all elements from the array. First, the adjacent triplet (2, 3, 4) is removed. The array is now reduced to [-1, 0, 1], which forms another valid triplet and can be removed from the array.
'''

def shrink(arr, k):

    win_size = 3

    # difine the pointers (indices that for the window)
    left, right = 0, len(arr) - win_size - 1

    while right <= len(arr)-1:
        
        x, y, z = arr[left], arr[left]+k, arr[right] # initialize values in the window
        
        # evaluate the condition then slide then window 
        if x + k == y and y + k == z:

            arr[left:right+1] = [] # shrink by removing the windowers of new window by moving left poiter a step back

            # init points
            left -= 1 
            
            right = left + 2

        else:
            left += 1 # move left pointer a step forward to slide the window

            right += 1 # move left pointer a step forward to slide the window

    return len(arr)         


if __name__ == '__main__':
 
    # arr = [1, 2, 3, 5, 7, 8]
    # arr = [-1, 0, 1, 2, 3, 4]
    arr = [-1, 2, 5, 8, 2, 5]
    k = 3
 
    print(shrink(arr, k))

