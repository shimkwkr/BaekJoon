# 1450 냅색문제
import sys
input = sys.stdin.readline

def combi(arr, temp, n, result):
    if n == len(arr):
        result.append(temp)
        return

    temp+=arr[n]
    combi(arr, temp, n + 1, result)
    temp-=arr[n]
    combi(arr, temp, n + 1, result)

    return result

N, C = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
cnt = 0


# 가방에 들어갈수 있는 무게가 0일때
if C == 0:
    print(1)
    exit()

# 가방에 넣을수 있는 물건이 1개뿐일때
if N == 1:
    if lst[0] <= C:
        print(2)
    else:
        print(1)
    exit()

# 그 이외의 모든 상황에 대하여
left = sorted(combi(lst[:N//2], 0, 0, []))
right = sorted(combi(lst[N//2:], 0, 0, []), reverse=True)

ln_l = len(left)
ln_r = len(right)

l_s, r_s = 0, 0
while l_s < len(left) and r_s < len(right):
    # 합이 C보다 큰경우 right를 한칸 이동
    if left[l_s] + right[r_s] > C:
        r_s += 1
    # 합이 C와 같거나 작은 경우
    else:
        temp_l, temp_r = l_s, r_s
        # left 부터 같은 수가 몇개있는지 파악
        while left[temp_l] == left[l_s]:
            temp_l += 1
            if temp_l == ln_l:
                break

        # cnt 업데이트
        cnt += (temp_l - l_s) * (ln_r - r_s)

        # 합이 C와 같은 경우 right를 조정하여 갱신
        # 합이 C보다 작은 경우 right를 조정할 필요가 x
        if left[l_s] + right[r_s] == C:
            # right 같은 수가 몇개 있는지 파악 후 r_s 갱신
            while right[temp_r] == right[r_s]:
                temp_r += 1
                if temp_r == ln_r:
                    break
            r_s = temp_r

        # l_s 갱신
        l_s = temp_l
print(cnt)