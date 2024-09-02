from collections import defaultdict

def solution(clothes):
    answer = 0
    cloth_dict = defaultdict(list)
    
    for cloth_name, cloth_type in clothes: # 의상 종류를 기준으로 딕셔너리 만들기
        cloth_dict[cloth_type].append(cloth_name)
    
    # print(cloth_dict) 

    combin = 1 
    for cloth_type in cloth_dict: # 경우의 수 구하기
        combin *=(len(cloth_dict[cloth_type])+1)
    combin -= 1 

    answer = combin
    return answer


clothes = [["yellow_hat", "headgear"], 
 ["blue_sunglasses", "eyewear"], 
 ["green_turban", "headgear"]]
result = solution(clothes)
print(result)


# 기본 딕셔너리 vs defaultdict 차이점 
# : 기본에서는 존재하지 않는 키를 조회할 경우 keyError가 발생
# : defaultdict는 기본값을 자동으로 생성할 수 있도록 설정 가능


