
def selectionSort(arr):
    for i in range (0,len(arr)):
        min=i                               #min value's index
        for j in range(i+1,len(arr)):       #searching min value
            if arr[j]<arr[min]:             #if found, change min index to j
                min=j

        arr[i], arr[min]=arr[min],arr[i]    #swap min value and index i's value



if __name__=="__main__":

    arr=[8,7,9,2,3,1,5,4,6]

    selectionSort(arr)
    print(arr)
