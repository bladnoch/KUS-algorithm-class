def merge(A, left, mid, right):

    # save left arr
    L = A[left:mid+1]

    # save right arr
    R = A[mid+1:right+1]

    # points elements that needs to compare
    i = j = 0

    # save first value in arr
    # it moves when element is organized
    k = left

    # check the size of values and compares
    while i < len(L) and j < len(R):

        #if L is smaller, put element of L into arr A
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1

        # if R is smaller, put R element into arr A
        else:
            A[k] = R[j]
            j += 1
        k += 1

    # merge arr
    print("legt: ",i, len(L))
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    print("right: ", i, len(R))
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1


# param: arr, first element, last element
def merge_sort(A, left, right):
    if left<right :
        # this will use when cut arr in half
        mid = (left + right) // 2

        merge_sort(A, left, mid)
        merge_sort(A, mid + 1, right)

        merge(A, left, mid, right)


if __name__=="__main__":

    # sample arr
    a=[40,5,79,2,8,341,2456,13,46]

    # param: arr, first element, last element
    merge_sort(a,0,(len(a)-1))
    print(a)