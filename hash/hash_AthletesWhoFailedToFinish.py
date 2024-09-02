from collections import Counter

def solution(participant, completion):
    answer = ''
    partic = Counter(participant) # 중복 값 포함 선수 수 파악
    comple = Counter(completion)  # 중복 이름 포함 선수 수 파악

    faild_per = partic - comple # 완주하지 못한 한 사람 
    keys_list = list(faild_per.keys())  # 딕너셔리로 정리되어 있기 때문에 정리 필요
    answer = keys_list[0]
    return answer

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
result = solution(participant, completion)
print(result)