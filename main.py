import asyncio
from music_recognition.recognizer import recognize_song
from emotion_analysis.analyzer import analyze_emotion
from video_player.player import play_animation

async def process_song(audio_file_path):
    song_info = await recognize_song(audio_file_path)
    if song_info:
        print(f"Recognized: {song_info}")
        emotion = analyze_emotion(song_info['genre'])
        frames_directory = f'animations/{emotion}'
        play_animation(frames_directory, audio_file_path, 30)  # Assuming 30 FPS for animation
    else:
        print("Song recognition failed.")

def main():
    audio_file_path = 'music_recognition/Test1.mp3'  # Start with one song to simplify
    asyncio.run(process_song(audio_file_path))

if __name__ == "__main__":
    main()
