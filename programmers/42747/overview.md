## H-Index
https://school.programmers.co.kr/learn/courses/30/lessons/42747

## 문제 이해
- H-Index: 어떤 과학자가 발표한 논문 n편 중 h번 이상 인용된 논문이 h편 이상일 때, h의 최댓값
    - 나머지 논문이 h번 이하 인용되는 조건은 항상 만족되므로 고려해야 하는 조건은 아님
    - ⚠️ h가 반드시 citations에 포함된 값인 것은 아님에 유의
        - 예: [4, 0, 6, 1, 5]인 테스트 케이스의 결과 기댓값은 3이고, 3은 citations에 없는 값임

## 전략 1: ${O(N^2)}$
- h를 논문별 인용 횟수 최댓값에서 시작하여 0까지 내려가며 H-Index를 계산
    - 이때, 논문의 수가 1000편 이하이므로 h의 최댓값은 1000이 됨
    - 필터 함수를 통해 citations의 각 원소들 중 h 이상인 원소들만 남겨두고 길이가 h 이상인지 확인
    - 위 확인 과정을 통과한 h 값이 있다면, 그 h 값을 반환
    - 반복문이 끝난다면 이는 h가 0임을 의미
- 시간 복잡도는 ${O(N^2)}$
    - 최대 논문의 수가 1000편이므로 citations의 최대 길이가 1000
    - 필터 함수는 citations의 각 원소를 순회하므로, 최대 1000번 순회
    - 따라서 최악의 경우 시행 횟수가 ${1000 \times 1000 = 1000000}$
    - 그런데, 시행 횟수 1000000번인 경우 보통 시간 초과가 발생하지 않음
    - 따라서, 여기서는 비록 시간 복잡도가 ${O(N^2)}$ 이지만 시간 초과가 발생하지는 않을 것이라 판단하여 ${O(N^2)}$ 알고리즘을 사용하였음

## 전략 2 (🗒️)
- 문제에서 제시된 출처(영문 위키백과)에 따르면 H-Index를 구하는 방법은 다음과 같음
    - 인용 횟수를 내림차순 정렬함
    - h를 변수로 하여 h번째 논문의 인용 횟수를 나타내는 함수 ${f}$
    - H-Index는 h를 1로 시작하여, 각 위치의 논문 인용 횟수와 비교했을 때, 그 논문의 인용 횟수가 h보다 큰 마지막 h를 의미함
        - 수식으로 정리하면 ${\max\{h \in \mathbb{N} : f(h) \geq i\}}$
- 위 방법을 따라서 H-Index를 구해보면 h는 점점 증가하지만, 논문의 인용 횟수는 점점 감소하며 둘 간의 차이가 가장 작은 지점이 생김
- 그 지점에서 둘 중 더 작은 값을 H-Index로 선택
- 전략 2는 이 전략을 바탕으로, h와 논문 인용 횟수 중 더 작은 값을 구해 가능한 H-Index들을 먼저 추려낸 후, 그 중 최댓값을 구하는 방식으로 접근함
- 아래 그림을 참고
- ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FuCJay%2FbtrFpuHY7Bg%2FAAAAAAAAAAAAAAAAAAAAAKZvMozFeFXE3Mctu67URzqWl8QWZi1-9kfZ9Bs-9KcO%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1772290799%26allow_ip%3D%26allow_referer%3D%26signature%3Dv8Hu6YuQFdDX6fThbekK%252F2SQ0s0%253D)

## 전략 3: 이진 탐색 (🗒️)
- h를 끼워넣는다고 가정하고, h를 끼워넣은 곳의 오른쪽 배열의 길이가 h보다 클 때 h의 최댓값을 반환하는 방식
    - ⚠️ 정렬이 오름차순으로 되어 있음
- `bisect.bisect_left(a, x)`: 정렬된 순서가 유지되도록 x를 a에 삽입할 때 a의 삽입 위치를 찾는 함수
    - x가 a에 없으면, 삽입 위치를 반환하고
    - x가 a에 있으면 가장 첫번째로 나타나는 x의 위치를 반환함
    - 여기서는 오름차순 정렬이므로 `bisect_left`를 사용