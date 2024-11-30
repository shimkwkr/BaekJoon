# 2343 기타레슨

def bin_srch(start, end):
    result = float('inf')
    temp = 0 
    while start <= end:
        m = 0
        mid = (start+end) //2
        # 현재의 mid(블루레이 길이)를 가지고 m이 몇개로 나누어지는지 확인
        for i in lecture:
            temp += i
            if temp > mid:
                temp = i

                m += 1
            elif temp == mid:
                temp = 0
                m += 1
        if temp != 0:
            temp = 0
            m += 1        
        # 나눙어진 m값을 기준으로 start, end를 조정
        if m > M:
            start = mid+1
        elif m == M:
            if end == mid:
                break
            end = mid
            # result값이 mid보다 크다면 갱신
            if result > mid:
                result = mid
        else:
            end = mid - 1

    if result == float('inf'):
        result = mid
            
    return result      
        

# N은 강의수, M은 강의수
N, M = map(int, input().split())
lecture = list(map(int, input().split()))

print(bin_srch(max(lecture), sum(lecture)))