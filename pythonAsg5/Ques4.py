#Ques 4
#Defining Quicksort Function
def QuickSort(array,low,high):
    if(low>=high): #If a single element or no element is there return
        return
    pivot=low #Creating a Variable with value of start
    count=low #Creating a Variable with value of start
    for i in range(low+1,high): #Counting number of terms less than or equal to pivot point
        if(array[i]<=array[pivot]):
            count+=1
    temp=array[pivot] #Substituting the value at pivot point with value at start
    array[pivot]=array[count]
    array[count]=temp
    pivot=count #replacing the previous value of pivot point with count
    i=low #defining two variable one from start and another from end
    j=high-1
    while(i<pivot and j>pivot):
        if(array[i]>array[pivot] and array[j]<=array[pivot]):
            temp = array[i] #Creating a while loop to shift number less than or equal to pivot on its left and greater than that on its right
            array[i] = array[j]
            array[j] = temp
            i+=1
            j-=1
        elif(array[j]>array[pivot]):
            j-=1
        elif(array[i]<=array[pivot]):
            i+=1
    QuickSort(array,low,pivot) #sorting left part of pivot
    QuickSort(array,pivot+1,high) #sorting right part of pivot

def Mergesort(array,start,end):
    size=end-start #size is defined
    if(size<=1): #if size of list is less than or equal to 1 return
        return
    else:
        mid=(start+end)//2  #defined a mid which is having value equal to (start+end)/2 floor division

        Mergesort(array,start,mid) #Calling the function for the left half part
        Mergesort(array,mid,end) #Calling the function for the right half part
        result=[0]*size #created a new list of the size equal to the size of input list
        i=start #Starting variable defined
        j=mid #another variable with value of mid is defined
        count=0
        # While loop is created for sorting the elements across the array if the starting index is less than mid and ending index is less than end index
        while(i<mid and j<end):
            if(array[i]<=array[j]):
                result[count]=array[i]
                i+=1
            elif(array[i]>=array[j]):
                result[count]=array[j]
                j+=1
            count+=1
        if(i==mid and j<end):#If the starting point is equal to mid but the end point is not equal to end of list
            while(j<end):
                result[count]=array[j]
                j+=1
                count+=1
        if (j == end and i < mid): #If the starting point is not equal to mid but the ending index is at end of the list
            while (i < mid):
                result[count] = array[i]
                i+=1
                count+=1

        for i in range(size): #Replacing the elements of the original list with the new list
            array[i+start]=result[i]
list1=list(map(int,input("Enter The Numbers:\n").split()))
print("List Entered By User:",list1) #Printing the input list
Mergesort(list1,0,len(list1)) #Using Merge Sort to sort the list
print("Sorted List Using Merge Sort:",list1)
QuickSort(list1,0,len(list1)) #Using Quick Sort to sort the list
print("Sorted List Using Quick Sort:",list1)
