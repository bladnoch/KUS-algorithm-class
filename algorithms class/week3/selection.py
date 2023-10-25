


def selectionSort(arr):
    for i in range (0,len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j

        arr[i], arr[min]=arr[min],arr[i]



if __name__=="__main__":

    arr=[8,7,9,2,3,1,5,4,6]

    for i in arr:
        selectionSort(arr)

    print(arr)
