import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
GREEN = (0, 200, 0)
SIDEBAR_BG = (230, 230, 230)

def draw_board(screen, board, cell_size, margin):
    for y in range(board.height):
        for x in range(board.width):
            color = GREEN if board.grid[y][x] == 1 else WHITE
            rect = pygame.Rect(
                x * (cell_size + margin) + margin,
                y * (cell_size + margin) + margin,
                cell_size,
                cell_size
            )
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)  # Grid lines

def draw_sidebar(screen, board, sidebar_width, board_width_px, board_height_px):
    font = pygame.font.SysFont(None, 20)
    sidebar_x = board_width_px
    pygame.draw.rect(screen, SIDEBAR_BG, (sidebar_x, 0, sidebar_width, board_height_px))

    lines = [
        "Controls:",
        "Space: Play/Pause",
        "N: Next Step",
        "C: Clear Board",
        "R: Random Fill",
        "S: Save Pattern",
        "L: Load Glider",
        "G: Start GIF",
        "H: Stop GIF",
        "",
        f"Generation: {board.generation if hasattr(board, 'generation') else 'N/A'}",
        f"Live Cells: {sum(sum(row) for row in board.grid)}"
    ]

    for i, line in enumerate(lines):
        label = font.render(line, True, BLACK)
        screen.blit(label, (sidebar_x + 10, 10 + i * 25))
