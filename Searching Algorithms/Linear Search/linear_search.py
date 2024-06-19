
"""
 Searching: it way to finding the given element in particular collections. If element exists then return the index, otherwise return -1

 Linear Search: Linear Search is a method for searching an element in a collection of elements.
                In Linear Search, each element of the collection is visited one by one in a sequential fashion to find the desired element.
                Linear Search is also known as Sequential Search.

                Steps:
                Start: Begin at the first element of the collection of elements.
                Compare: Compare the current element with the desired element.
                Found: If the current element is equal to the desired element, return true or index to the current element.
                Move: Otherwise, move to the next element in the collection.
                Repeat: Repeat steps 2-4 until we have reached the end of collection.
                Not found: If the end of the collection is reached without finding the desired element, return that the desired element is not in the array.


"""

# linear search
def linear_search(key=None, arr=None):

    i = 0

    len_arr = len(arr)
    total_iteration = 0

    while i < len_arr:
        current_val = arr[i]

        # if key is matched with current value then return index
        if(current_val == key):
            return {
                'total_iteration': total_iteration,
                'index': i
            }
        
        # increment i with one
        i += 1
        total_iteration += 1
    # if after performing all iteration key is not matched then return -1

    return {
                'total_iteration': total_iteration,
                'index': -1
            }

# binary search
def binary_search(key, arr:list):

    start  = 0
    end    = len(arr) -1

    mid    = start + ((end -start) // 2)
    
    # for testing purpose only to monitor difference between linear search 
    total_iteration = 0

    while start <= end:

        # if arr of mid is equal to the key then return index of mid
        if(arr[mid] == key):
            return {
                'total_iteration': total_iteration,
                'index': mid
            }
        
        # key is greater than mid then go right part of the array
        elif(key > arr[mid]):
            start = mid + 1
        
        else:
            # means key is less than mid go left part
            end  = mid -1

        # count number of total interation for testing purpose only
        
        

        # update the mid
        mid = start + ( (end-start)// 2)

        # for testing only
        total_iteration += 1
    
    return {
                'total_iteration': total_iteration,
                'index': -1
            }





key = 99966

arr2 = [2,5,8,12,13,24,27]
arr3 = [12,13,34,45,56,76,78,89, 91, 99, 101]

arr4 = [n for n in range(1, 100001)]
print(arr4)

linear_search_result = linear_search(key=key, arr=arr4)
binary_search_result = binary_search(key=key, arr=arr4)

print(f'Actual Impact/difference:\n linear-search {linear_search_result} \n binary search: {binary_search_result}  ')


# binary search complexity = O(log n) in worse case
# linear search complexity = O(N)     in worse case

"""
    Output:

    Actual Impact/difference:
        linear-search {'total_iteration': 99965, 'index': 99965} 
        binary search: {'total_iteration': 16, 'index': 99965} 
"""