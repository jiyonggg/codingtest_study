## 같은 숫자는 싫어
https://school.programmers.co.kr/learn/courses/30/lessons/12906

## 전략
- 배열을 순회하면서, 정답 배열의 마지막 원소가 지금 원소와 다를 때 정답 배열에 append
    - 예외 처리: 정답 배열이 비어있는 상태의 경우 IndexError 남
        - -> if 조건 (OR) 
            - 정답 배열이 비어있음
            - 정답 배열 마지막 원소가 반복문 내 현재 원소와 다름