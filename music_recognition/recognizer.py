from shazamio import Shazam

async def recognize_song(audio_file_path):
    shazam = Shazam()
    out = await shazam.recognize_song(audio_file_path)

    # Extracting information from the response
    track = out['track']
    title = track['title']
    artist = track['subtitle']
    genre = track.get('genres', {}).get('primary', 'Unknown')

    return {
        'title': title,
        'artist': artist,
        'genre': genre
    }
