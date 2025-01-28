import pygame
import os
from pygame import mixer

def play_animation(frames_directory, audio_file_path, frame_rate=30):
    pygame.init()
    mixer.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Dance Animation')

    mixer.music.load(audio_file_path)
    mixer.music.play()

    while not mixer.music.get_busy():
        pygame.time.delay(100)

    frames = []
    for frame_file in sorted(os.listdir(frames_directory)):
        if frame_file.endswith('.png'):
            frame_path = os.path.join(frames_directory, frame_file)
            try:
                frame = pygame.image.load(frame_path)
                frames.append(frame)
            except Exception as e:
                print(f"Error loading {frame_path}: {e}")

    clock = pygame.time.Clock()
    for frame in frames:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.blit(frame, (0, 0))
        pygame.display.flip()
        clock.tick(frame_rate)

    mixer.music.stop()
    pygame.quit()
