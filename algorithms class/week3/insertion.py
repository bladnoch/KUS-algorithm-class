

def insertion(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j-1] >arr[j] and j >0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1





if __name__=="__main__":
    arr=[8,7,9,2,3,1,5,4,6]
    insertion(arr)
    print(arr)