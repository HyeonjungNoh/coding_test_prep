def solution(nums):
    answer = 0
    total = len(nums) # 전체 포켓몬 수
    pick_mix = total//2 # 최대 가져갈 수 있는 포켓몬 수
    Ntypes = len(set(nums)) # 종류의 개수

    if pick_mix <= Ntypes:
        answer = pick_mix
    else:
        answer = Ntypes
    return answer


nums = [3,1,2,3]
result = solution(nums)
print(result)



# 다른 사람 풀이 
# def solution(ls):
#     return min(len(ls)/2, len(set(ls)))
## 미텼다... 완전 간결하네