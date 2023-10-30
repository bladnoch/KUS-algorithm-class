def quickselect(lst, left, right, k):

    #인덱스 길이가 같으면 바로 리턴
    if left == right:
        return lst[left]

    #best pivot 의 인덱스 찾기
    pivot_index = median_of_medians(lst, left, right)

    #pivot index partition 분할
    pivot_index = partition(lst, left, right, pivot_index)

    #k랑 피벗 인덱스가 같으면 k 리턴
    if k == pivot_index:
        return lst[k]
    #k가 더 작으면 왼쪽 파티션 사용
    elif k < pivot_index:
        return quickselect(lst, left, pivot_index - 1, k)
    #더 크면 오른쪽 파티션 사용
    else:
        return quickselect(lst, pivot_index + 1, right, k)

def median_of_medians(lst, left, right):

    #길이가 5 이하일 경우 partition5 함수 실행
    if right - left < 5:
        return partition5(lst, left, right)

    #리스트의 요소를 5개씩 사용해서 각각 중간값을 찾으며 반복
    for i in range(left, right + 1, 5):
        #오른쪽 끝 인덱스를 저장 길이가 부족할경우를 대비
        sub_right = min(i + 4, right)
        median5 = partition5(lst, i, sub_right)

        #중간값을 리스트 왼쪽으로 이동
        lst[median5], lst[left + (i - left) // 5] = lst[left + (i - left) // 5], lst[median5]

    #중간의 중간값을 찾기위한 값을 quickselect 함수로 리턴
    return quickselect(lst, left, left + (right - left) // 5, left + (right - left) // 10)


def partition5(lst, left, right):
    i = left + 1

    #주어진 인덱스에서 중간값을 찾아 인덱스 리턴
    while i <= right:
        key = lst[i]
        j = i - 1

        #insertion sort
        while j >= left and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1

        lst[j + 1] = key
        i += 1

    return left + (right - left) // 2

def partition(lst, left, right, pivot_index):

    # 피벗을 이용해 좌우를 정렬
    lst[right], lst[pivot_index] = lst[pivot_index], lst[right]
    pivot = lst[right]
    i = left - 1

    for j in range(left, right):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[i + 1], lst[right] = lst[right], lst[i + 1]
    return i + 1

if __name__=="__main__":

    lstII=[2,3,4,5,6,1,8,9,0,7]
    k = 7 #k번째로 작은 요소

    print("list = "+str(lstII))
    print("k(k th smallest number) = "+str(k))
    print("result = "+str(quickselect(lstII,0,len(lstII)-1,k-1)))