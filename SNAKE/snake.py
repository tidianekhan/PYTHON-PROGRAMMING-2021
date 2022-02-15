import snakelib

width = 0  # initialized in play_snake
height = 0  # initialized in play_snake
ui = None  # initialized in play_snake
SPEED = 10
keep_running = True
length_of_snake = [[0, 0], [0, 1]]
apple_position = (-1, -1)


def play_snake(init_ui):
    global width, height, ui, keep_running, apple_position, length_of_snake
    def find_apple():
        global apple_position
        global length_of_snake

        l = length_of_snake
        a = [[0] * width for x in range(height)]

        def create_list():
            t = 0
            for x in range(height):
                for y in range(width):
                    if [x, y] not in l:
                        a[x][y] = c
                        t += 1
                    else:
                        a[x][y] = "S"
            return t

        def correct_coordinates(n):
            for x in range(height):
                for y in range(width):
                    if a[x][y] == n:
                        return x, y

        apple_position=correct_coordinates(ui.random(create_list()))

    def place_apple():
        length_of_snake.append([y, x])
        find_apple()
        ui.place(x, y, ui.SNAKE)
        ui.place(apple_position[0], apple_position[1], ui.FOOD)
        ui.show()

    def draw(x, y):
        ui.place(x, y, ui.SNAKE)
        if [y, x] in length_of_snake and [y, x] != length_of_snake[0]:
            ui.set_game_over()
        elif [y, x] == length_of_snake[0]:
            length_of_snake.append([y, x])
            length_of_snake.pop(0)
        else:
            length_of_snake.append([y, x])
            ui.place(length_of_snake[0][1], length_of_snake[0][0], ui.EMPTY)
            length_of_snake.pop(0)

        ui.show()

    ui = init_ui
    width, height = ui.board_size()
    x = 1
    y = 0

    find_apple()
    ui.place(0, 0, ui.SNAKE)
    ui.place(1, 0, ui.SNAKE)

    ui.place(apple_position[0], apple_position[1], ui.FOOD)
    ui.show()

    current_direction = "r"
    while keep_running:

        event = ui.get_event()
        left_border = 0
        upper_border = 0
        right_border = width - 1
        down_border = height - 1
        list_of_possible_moves = ["d", "u", "l", "r"]
        if event.name == "alarm":
            if x < right_border and current_direction == "r":
                x += 1
                if (x, y) == apple_position:
                    place_apple()
                else:
                    draw(x, y)
            elif x <= right_border and current_direction == "l" and x != 0:
                x -= 1
                if (x, y) == apple_position:
                    place_apple()
                else:
                    draw(x, y)
            elif current_direction == "d" and y != down_border:
                y += 1
                if (x, y) == apple_position:
                    place_apple()
                else:
                    draw(x, y)
            elif current_direction == "u" and y != upper_border:
                y -= 1
                if (x, y) == apple_position:
                    place_apple()
                else:
                    draw(x, y)
            elif current_direction == "u" and y == upper_border:
                y = down_border
                if (x, y) == apple_position:
                    place_apple()
                else:
                    draw(x, y)
            elif current_direction == "d" and y == down_border:
                y = upper_border
                if (x, y) == apple_position:
                    place_apple()
                else:
                    draw(x, y)
            elif x == left_border:
                x = right_border
                if (x, y) == apple_position:
                    place_apple()
                else:
                    draw(x, y)
            elif x == right_border:
                x = left_border
                if (x, y) == apple_position:
                    place_apple()
                else:
                    draw(x, y)
        if event.name == "quit":
            keep_running = False
        elif event.data in list_of_possible_moves:
            current_direction = event.data


if __name__ == "__main__":
    # do this if running this module directly
    # (not when importing it for the tests)
    ui = snakelib.SnakeUserInterface(10, 10)
    ui.set_animation_speed(SPEED)
    play_snake(ui)