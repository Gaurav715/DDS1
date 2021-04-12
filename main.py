# Python program for implementation of BubbleSort
def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Python program for implementation of InsertionSort
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 


# Python program for implementation of MergeSort 
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
                
                
                
# Python program for implementation of SelectionSort 
def selectionSort(arr):

   for i in range(len(arr)):

      # Find the minimum element in remaining
       minPosition = i

       for j in range(i+1, len(arr)):
           if arr[minPosition] > arr[j]:
               minPosition = j
                
       # Swap the found minimum element with minPosition       
       temp = arr[i]
       arr[i] = arr[minPosition]
       arr[minPosition] = temp

   return arr
               
                
# Example to test code above
arr1 = [64, 34, 25, 12, 22, 11, 90, 123, 42134, 342,-2]
 
# bubbleSort(arr1)
# selectionSort(arr1)
mergeSort(arr1)
#selectionSort(arr1)
 
print ("Sorted array is:")
for i in range(len(arr1)):
    print (arr1[i]), 