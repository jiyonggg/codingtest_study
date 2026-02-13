from collections import defaultdict

class GenreInfo:
    def __init__(self):
        self.song_counts = dict()
    
    @property
    def total(self):
        return sum(self.song_counts.values())
    
    def add_song_count(self, song_no, count):
        self.song_counts[song_no] = count

def solution(genres, plays):
    genre_map = defaultdict(GenreInfo)

    for i in range(len(genres)):
        genre = genres[i]
        count = plays[i]

        genre_map[genre].add_song_count(i, count)

    answer = []

    genre_sorted = sorted(genre_map.keys(), key=lambda x: genre_map[x].total, reverse=True)

    for genre in genre_sorted:
        songs_sorted = sorted(genre_map[genre].song_counts.keys(), key=lambda x: genre_map[genre].song_counts[x], reverse=True)
        answer.extend(songs_sorted[:2])

    return answer