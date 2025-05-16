import pygame

def handle_events(event, board):
    """
    Returns:
        running (bool): whether to keep running
        pause (bool): current pause state
        action (str or None): 'save', 'load', 'gif_start', 'gif_stop' or None
    """
    running = True
    pause = False
    action = None

    # Track pause state outside to maintain toggle
    if not hasattr(handle_events, "pause"):
        handle_events.pause = False

    if event.type == pygame.QUIT:
        running = False

    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            handle_events.pause = not handle_events.pause
        elif event.key == pygame.K_c:
            board.clear()
        elif event.key == pygame.K_r:
            board.random_fill()
        elif event.key == pygame.K_n:
            board.next_generation()
        elif event.key == pygame.K_s:
            action = "save"
        elif event.key == pygame.K_l:
            action = "load"
        elif event.key == pygame.K_g:
            action = "gif_start"
        elif event.key == pygame.K_h:
            action = "gif_stop"

    pause = handle_events.pause
    return running, pause, action
