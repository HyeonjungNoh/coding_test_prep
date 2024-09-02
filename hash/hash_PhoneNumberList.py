def solution(phone_book):
    answer = True
    phone_book.sort() # 정렬 필수. 정렬시 인전한 전화번호들만 비교하는 방법
    for i in range(len(phone_book)-1):
        # print(i)
        # print(phone_book[i])
        if phone_book[i+1].startswith(phone_book[i]):
            answer = False
   
    return answer



# phone_book = ["119", "97674223", "1195524421"]
phone_book = ["123","456","789"] 
# phone_book = ["12","123","1235","567","88"]
result = solution(phone_book)
print(result)








# def solution(phone_book):
#     answer = True
#     prefix = phone_book[0]

#     for str in phone_book[1:]:
#         if str.startswith(prefix) == False:
#             answer = "false"
#             break
#         else:
#             continue
#     answer = "true"

#     return answer