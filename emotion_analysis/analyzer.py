 # emotion_analysis/analyzer.py
def analyze_emotion(song_genre):
    genre_emotion_map = {
        'Pop': 'happy',
        'Blues': 'sad',
        'neutral':'happy',
        "Children's Music":"happy",
        # Add more mappings as needed
    }
    return genre_emotion_map.get(song_genre, 'nothing')
