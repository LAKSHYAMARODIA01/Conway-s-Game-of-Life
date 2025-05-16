import pygame
import imageio
import numpy as np

class GIFRecorder:
    def __init__(self, filename="game_of_life.gif"):
        self.frames = []
        self.filename = filename
        self.recording = False

    def start(self):
        print("Started GIF recording...")
        self.frames = []
        self.recording = True

    def stop(self):
        self.recording = False
        if self.frames:
            imageio.mimsave(self.filename, self.frames, duration=0.1)
            print(f"GIF saved as {self.filename}")
        else:
            print("No frames recorded.")

    def capture_frame(self, surface):
        if not self.recording:
            return
        # Convert pygame surface to numpy array
        data = pygame.surfarray.array3d(surface)
        # Transpose and convert to uint8 RGB
        frame = np.transpose(data, (1, 0, 2))
        self.frames.append(frame)
