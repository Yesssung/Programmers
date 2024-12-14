# 1. 중복된 숫자 개수
# 내가 쓴 답
# def solution(array, n):
#     answer = array
#     print(answer.count(n))
#
#     return answer
from sqlalchemy.dialects.mysql import insert


# 답
# def solution(array, n):
#     answer = array.count(n)         # n의 개수를 계산
#
#     return answer                   # 개수를 반환

# 풀이
# def solution ()라는게 array 와 n이 이미 있고 그게 매개변수로 전달된다는 뜻
# 전달된 매개변수를 answer에 저장
# array 에 n의 개수가 몇개인지 count 하기
# 결과를 return하기


# 2. 나머지 구하기
# 내가 쓴 답
# def solution(num1, num2):
#     answer = num1 % num2
#     return answer
# 답
# PASS


# 3. 문자열로 반환
# 내가 쓴 답
# def solution(n):
#     answer = str(n)
#     return answer
# PASS
# 정수로 주어진 n을 str 붙여서 문자열로 반환!


# 4. 홀짝에 따라 다른 값 반환하기
# 모범 답안............
# def solution(n):
#     if n%2:
#         return sum(range(1,n+1,2))
#     return sum([i*i for i in range(2,n+1,2)])

# 5. 나이 출력
def solution(age):
    answer = 2022 - (age-1)
    return answer