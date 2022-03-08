#Ques 5
#Using Merge Sort to Sort The list
def Mergesort(array,start,end):
    size=end-start
    if(size<=1):
        return
    else:
        mid=(start+end)//2

        Mergesort(array,start,mid)
        Mergesort(array,mid,end)
        result=[0]*size
        i=start
        j=mid
        count=0
        while(i<mid and j<end):
            if(array[i]<=array[j]):
                result[count]=array[i]
                i+=1
            elif(array[i]>=array[j]):
                result[count]=array[j]
                j+=1
            count+=1
        if(i==mid and j<end):
            while(j<end):
                result[count]=array[j]
                j+=1
                count+=1
        if (j == end and i < mid):
            while (i < mid):
                result[count] = array[i]
                i+=1
                count+=1

        for i in range(size):
            array[i+start]=result[i]

#BinarySearch Function
def Binarysearch(list,number):
    start=0
    end=len(list)
    indicator=False
    while(start<=end):
        mid=(start+end)//2
        if(list[mid]==number):
            indicator=True
            break
        elif(list[mid]>number):
            end=mid-1
        elif(list[mid]<number):
            start=mid+1
    return indicator

#Taking Input of list from User and converting it into list directly
input_list=list(map(int,input("Enter The Numbers:\n").split()))
print("List Entered By User:",input_list)
#Sorting the list using Merge Sort
print("Part a")
Mergesort(input_list,0,len(input_list))
print("Sorted List:",input_list)
#Taking Input from user to check the number
number_check=int(input("Enter The Number You Want To Check:\n"))

#Printing the result, if the number present in the list entered by user using binary search
print("Part b")
print("If the Number is Present:",Binarysearch(input_list,number_check))
#Counting the number of times the number has appeared in list
print("Part c")
if(Binarysearch(input_list,number_check)==True):
     print("Number of times the number entered by user appeared:",input_list.count(number_check))
