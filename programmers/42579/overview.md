## 베스트앨범
https://school.programmers.co.kr/learn/courses/30/lessons/42579

## 전략 1
- 주어진 데이터를 JSON 형태로 나타냈다고 생각해보기
```json
"genres": {
    "classic": {
        "total": 1450,
        "song_count": {
            "0": 500,
            "2": 150,
            "3": 180
        }
    },
    "pop": {
        "total": 3100,
        "song_count": {
            "1": 600,
            "4": 2500
        }
    }
}
```
- 위와 같은 느낌으로 나타날 것임
- 반복되는 total, song_count 정보는 하나의 클래스 (`GenreInfo`)를 만들어 저장
    - total의 경우, song_count의 값의 총합과 같으므로, `@property`로 선언해서 필요할 때 계산
- 먼저, total을 기준으로 내림차순 정렬
- 각 장르의 `GenreInfo`에 대해서 song_count의 키(곡 번호)를 값(재생 횟수) 기준으로 내림차순 정렬
- 정렬한 song_count의 키들을 `[:2]`로 슬라이싱
- 정답으로 반환할 리스트에 슬라이싱한 것을 extend