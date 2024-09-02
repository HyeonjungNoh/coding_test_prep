import numpy as np
from collections import defaultdict

def solution(genres, plays):
    answer = []
    plays_index = list(enumerate(plays)) # 노래와 노래의 고유번호(인덱스) 같이 저장
 
    GC_array =list(zip(genres, plays_index)) # 장르랑 노래 2차원 배열로 만들기 


    album_dict = defaultdict(list) # 장르별로 노래 딕션너리 만들기
    for genre, play in GC_array:
        album_dict[genre].append(play)
    # --> {'classic': [(0, 500), (2, 150), (3, 800)], 'pop': [(1, 600), (4, 2500)]})


    # 각 장르별 총 재생 횟수 구한 후,
    total_plays = {}
    for g, s in album_dict.items():
        total_plays[g] = sum(y for _, y in s)

    # 총 재생 횟수를 기준으로 장르 내림차순으로 정렬
    sorted_genres= sorted(total_plays.items(), key=lambda item: item[1], reverse=True)

    final_album_dict = {} # 장르, 노래 재생수, 내림차순으로 정렬 끝(최종 딕셔너리)
    for gen, _ in sorted_genres:
        final_album_dict[gen] = sorted(album_dict[gen], key= lambda x:x[1], reverse=True)


    for genre, song in final_album_dict.items(): # 내림차순으로 정렬된 딕셔너리,각 장르별 두개씩 뽑기
        for s in song[:2]:
            answer.append(s[0])
     
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
result = solution(genres, plays)
print(result)



