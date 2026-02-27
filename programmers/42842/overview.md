## 카펫
https://school.programmers.co.kr/learn/courses/30/lessons/42842

## 전략
### 전략 1: 완전 탐색
- yellow는 노란색 칸들 전체의 테두리 가로와 세로의 곱과 같음
- 노란색 칸들 전체의 테두리 세로 길이를 기준으로 가능한 값들 순회
    - 우선, yellow에서 테두리 세로 길이를 나눴을 때 나누어 떨어져야 함
    - 카펫의 가로 길이가 세로 길이와 같거나 세로 길이보다 길기 때문에, 테두리 세로 길이의 최대는 yellow의 제곱근을 내림한 것

### 전략 2: 수학적 풀이 (🗒️)
- 이 문제에서 방정식 2개를 세울 수 있음
    - ${x \times y = yellow}$
    - ${2(x + y) = brown - 4}$
- 이 방정식 2개를 가지고 x에 대한 이차방정식을 만들어 근의 공식을 이용해서 풀어보면
    - ${x = \frac{-(4 - brown) \pm \sqrt{(4-brown)^2 - 16yellow}}{4}}$
- 가로가 세로보다 길기에,
    - ${x = \frac{-(4 - brown) + \sqrt{(4-brown)^2 - 16yellow}}{4}}$ 가 yellow의 테두리 가로 길이
    - ${x = \frac{-(4 - brown) - \sqrt{(4-brown)^2 - 16yellow}}{4}}$ 가 yellow의 테두리 세로 길이
- 카펫의 가로, 세로는 각각 yellow의 테두리 가로 길이, 세로 길이에 2를 더하면 됨