import pygame
import argparse
from board import Board
from draw import draw_board, draw_sidebar
from controls import handle_events
from persistence import save_pattern_to_file, load_pattern_from_file
from gif_recorder import GIFRecorder

# Constants
CELL_SIZE = 20
MARGIN = 1
SIDEBAR_WIDTH = 180
BG_COLOR = (245, 245, 245)

def parse_args():
    parser = argparse.ArgumentParser(description="Conway's Game of Life")
    parser.add_argument('--width', type=int, default=40, help='Number of cells horizontally')
    parser.add_argument('--height', type=int, default=30, help='Number of cells vertically')
    parser.add_argument('--fps', type=int, default=10, help='Frames per second')
    return parser.parse_args()

def main():
    args = parse_args()
    pygame.init()
    pygame.display.set_caption("Conway's Game of Life")

    # Calculate window size: board + sidebar
    board_width_px = args.width * (CELL_SIZE + MARGIN) + MARGIN
    board_height_px = args.height * (CELL_SIZE + MARGIN) + MARGIN
    window_width = board_width_px + SIDEBAR_WIDTH
    window_height = board_height_px

    screen = pygame.display.set_mode((window_width, window_height))
    clock = pygame.time.Clock()

    board = Board(args.width, args.height)
    board.random_fill()

    pause = False
    gif_recorder = GIFRecorder("game_of_life.gif")

    running = True
    while running:
        for event in pygame.event.get():
            running, pause, action = handle_events(event, board)
            if action == "save":
                save_pattern_to_file("patterns/saved_pattern.txt", board.get_live_cells())
            elif action == "load":
                pattern = load_pattern_from_file("patterns/glider.txt")
                board.clear()
                board.set_live_cells(pattern)
            elif action == "gif_start":
                gif_recorder.start()
            elif action == "gif_stop":
                gif_recorder.stop()

        if not pause:
            board.next_generation()

        # Draw board and sidebar
        screen.fill(BG_COLOR)
        draw_board(screen, board, CELL_SIZE, MARGIN)
        draw_sidebar(screen, board, SIDEBAR_WIDTH, board_width_px, board_height_px)

        pygame.display.flip()

        # Capture frame for GIF if recording
        gif_recorder.capture_frame(screen)

        clock.tick(args.fps)

    pygame.quit()

if __name__ == "__main__":
    main()
