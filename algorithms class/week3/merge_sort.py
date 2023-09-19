def merge_sort(arr):
    # 만약 arr의 길이가 1 이하라면 이미 정렬된 상태로 판단하고 그대로 반환합니다.
    if len(arr) <= 1:
        return arr

    # arr을 절반으로 나누어 left와 right에 저장합니다.
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # 각각의 반을 재귀적으로 계속해서 나눕니다.
    left = merge_sort(left)
    right = merge_sort(right)

    # 분할된 배열을 병합합니다.
    return merge(left, right)

def merge(left, right):

    # 병합 결과를 저장할 result 배열과
    # 왼쪽 배열과 오른쪽 배열을 가리킬 인덱스 i, j를 선언합니다.
    result = []
    i = j = 0

    # 왼쪽 배열과 오른쪽 배열 모두 순회할 동안 반복하는 while문입니다.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 왼쪽 혹은 오른쪽 배열 중 아직 순회하지 않은 요소가 있다면 결과에 추가해줍니다.
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1


    return result

if __name__=="__main__":
    # 주어진 데이터 확인
    data_list=[5,3,6,1,8,7,10,9,2]
    print(merge_sort(data_list))
