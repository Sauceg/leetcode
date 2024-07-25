#Merge Sort - Marvin Uwalaka
def mergeSort(nums): #This is the main function that sorts the Array
    #Base case for if the there is only one item in the array(the array as been devided to its lowest level)
    if len(nums) <= 1:
        return nums
    #Get the middle index of the array then slice it down the middle 
    mid = len(nums) // 2
    l1 = nums[:mid]
    l2 = nums[mid:]
    
    #Call mergeSort  on the sliced arrays 
    l1 = mergeSort(l1)
    l2 = mergeSort(l2)
    
    #Call the merge helper function on the sliced arrays 
    return merge(l1, l2)
        
def merge(l1,l2):
    i = 0
    j = 0
    merg = []
    
    #while loops sorts the subarrays by checking to see which index has the smaller element
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merg.append(l1[i])
            i += 1
        else:
            merg.append(l2[j])
            j += 1
    #if there are any elements left at the end of eaxh array add them to the merged array 
    if i < len(l1):
        merg += l1[i:]
    else:
        merg += l2[j:]
    #return the merged array of the sliced arrays 
    return merg
return mergeSort(nums)