class LifeGeneration:
    def __init__(self, state):
        self.matrix = state
        self.height = len(state)
        tmp = 0
        for row in state:
            if len(row) > tmp:
                tmp = len(row)
            else:
                pass

        self.width = tmp

    def board_width(self, width):
        return self.width

    def board_height(self, height):
        return self.height

    def is_alive(self, x, y):
        return self.matrix[y][x]

    def find_neighbors(self, x, y):
        living = 0

        for k, row in enumerate(self.matrix):
            if x - 1 <= k and k <= x + 1:
                for l, cell in enumerate(row):
                    if y - 1 <= l and l <= y + 1:
                        if cell and not (k == x and l == y):
                            living += 1


        return living

    def next_generation(self):

        following_state = [[False] * self.width for i in range(self.height)]

        for x, row in enumerate(self.matrix):
            for y, cell in enumerate(row):
                nbr = self.find_neighbors(x, y)


                if cell == True:
                    if nbr <= 1:
                        following_state[x][y] = False
                    elif nbr == 2 or nbr == 3:
                        following_state[x][y] = True
                    else:
                        following_state[x][y] = False

                else:
                    if nbr == 3:
                        following_state[x][y] = True
                    else:
                        following_state[x][y] = False

        return LifeGeneration(following_state)

    def is_all_dead(self):
        for row in self.matrix:
            for cell in row:
                if cell == True:
                    return False
        return True

    def board(self):
        return self.matrix


class LifeHistory:
    def __init__(self, first_gen):
        self.state = first_gen
        self.history = [first_gen]

        self.period_length = None

    def play_step(self):
        self.state = self.state.next_generation()
        self.history.append(self.state)

    def nr_generations(self):
        return len(self.history)

    def get_generation(self, n):
        for n in range(1, n):
            self.play_step()
        return self.state


    def dies_out(self):
        return self.state.is_all_dead()


    def period(self):
        return self.period_length


    def play_out(self, maximum_steps):
        for i in range(maximum_steps):
            self.play_step()

            entry = self.history[-1]

            if entry.is_all_dead() == True:
                return


            for index, past_state in enumerate(self.history[:-1]):
                if entry.board() == past_state.board():
                    self.period_length = i - index + 1
                    return

    def all_boards(self):
        twod = list()

        for i in self.history:
            twod.append(i.board())

        return twod