import snakelib

width = 0  # initialized in play_animation
height = 0  # initialized in play_snake
ui = None  # initialized in play_animation
SPEED = 1
keep_running = True


def erase_everything():
    ui.clear()


def draw(x, y, z):
    ui.clear()
    ui.place(x, y, z)
    ui.show()


def play_animation(init_ui):
    global width, height, ui, keep_running
    ui = init_ui
    width, height = ui.board_size()
    x = 0
    y = 0
    snake = ui.SNAKE

    draw(x, y, snake)
    while keep_running:
        # The animated object can't go the full width it has to go one less
        width_limit = width - 1
        length_limit = height - 1
        event = ui.get_event()
        if event.name == "alarm":
            if x < width_limit:
                x += 1
                draw(x, y, snake)
            elif y == length_limit:
                x = 0
                y = 0
                draw(x, y, snake)
            else:
                x = 0
                y += 1
                draw(x, y, snake)
        elif event.data == "space":
            if snake == ui.SNAKE:
                snake = ui.FOOD
            else:
                snake = ui.SNAKE
                # make sure you handle the quit event like below,
        # or the test might get stuck in an infinite loop
        if event.name == "quit":
            keep_running = False


if __name__ == "__main__":
    # do this if running this module directly
    # (not when importing it for the tests)
    ui = snakelib.SnakeUserInterface(10, 10)
    ui.set_animation_speed(SPEED)
    play_animation(ui)
