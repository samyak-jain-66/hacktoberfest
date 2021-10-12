"""
It is the most basic type of sorting algorithm in which we compare each element with its adjecent element and swap them
in each iteration we get a greatest value and the end.
Iterative Algorithm
Inplace Algorithm-->(we directly change inside main arr)
Time Complexity-->O(n^2)
"""
def bubble_sort(arr):
    for i in range(len(arr)-1):
        swapped=False
        for j in range(len(arr)-1-i):
            if(arr[j]>arr[j+1]):  # change sign to sort in decending order
                swapped=True
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if(not(swapped)):
            print("Sorting Complete")
            break
    print(arr)
    return arr


if __name__ == "__main__":
    arr=[2,5,8,6,1] #input 
    bubble_sort(arr)
