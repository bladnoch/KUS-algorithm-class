def bubble(arr):
    sorted=False
    while not sorted:
        sorted=True
        for i in range(0, len(arr)-1):
            if arr[i]>arr[i+1]:
                sorted=False
                arr[i],arr[i+1]=arr[i+1],arr[i]



if __name__=="__main__":
    arr=[8,7,9,2,3,1,5,4,6]
    bubble(arr)
    print(arr)