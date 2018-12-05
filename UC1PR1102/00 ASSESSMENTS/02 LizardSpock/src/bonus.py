"""
bonus.py
Eirik Rynning 2018
"""


import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random import randint

WIDTH = 60
HEIGHT = 30
SNAKE_LENGTH = 15
SNAKE_X = SNAKE_LENGTH + 1
SNAKE_Y = 3
SPEED = 90
MAX_X = WIDTH - 2
MAX_Y = HEIGHT - 2
KEY_MAP = {
    KEY_UP: KEY_DOWN, KEY_DOWN: KEY_UP,
    KEY_LEFT: KEY_RIGHT, KEY_RIGHT: KEY_LEFT,
}


class Snake():
    def __init__(self, x, y, window):
        self.body_list = []
        self.hit_score = 0
        self.timeout = SPEED
        # Adding the length of the snake to the body.
        for i in range(SNAKE_LENGTH, 0, -1):
            self.body_list.append(Body(x - i, y))
        # Adding the head of the snake as an "@"
        self.body_list.append(Body(x, y, "@"))
        # Defining the window
        self.window = window
        # Forcing snake to move to right when the game initializes.
        self.direction = KEY_RIGHT
        # Set the heads coordinates in the windows.
        self.last_head_coor = (x, y)
        # Defining the movement map.
        self.direction_map = {
            KEY_UP: self.move_up,
            KEY_DOWN: self.move_down,
            KEY_LEFT: self.move_left,
            KEY_RIGHT: self.move_right
        }


    def bodyadd(self, body_list):
        self.body_list.extend(body_list)

    def eat(self, food):
        food.reset()
        body = Body(self.last_head_coor[0], self.last_head_coor[1])
        self.body_list.insert(-1, body)
        self.hit_score += 1
        if self.hit_score % 3 == 0:
            self.timeout -= 5
            self.window.timeout(self.timeout)


    def update(self):
        """Creating animation updating function."""
        last_body = self.body_list.pop(0)
        last_body.x = self.body_list[-1].x
        last_body.y = self.body_list[-1].y
        self.body_list.insert(-1, last_body)
        self.last_head_coor = (self.head.x, self.head.y)
        self.direction_map[self.direction]()

    def new_direction(self, direction):
        if direction != KEY_MAP[self.direction]:
            self.direction = direction

    def add(self):
        for body in self.body_list:
            self.window.addstr(body.y, body.x, body.char)

    @property
    def collided(self):
        """Check if head has hit the Body"""
        return any([body.coor == self.head.coor
                    for body in self.body_list[:-1]])
    @property
    def head(self):
        """Places the head of snake in front of the body. """
        return self.body_list[-1]

    @property
    def coor(self):
        return self.head.x, self.head.y

    @property
    def score(self):
        return "Score: {}".format(self.hit_score)

    # Moving functions:

    def move_up(self):
        self.head.y -= 1
        if self.head.y < 1:
            self.head.y = MAX_Y

    def move_down(self):
        self.head.y += 1
        if self.head.y > MAX_Y:
            self.head.y = 1

    def move_left(self):
        self.head.x -= 1
        if self.head.x < 1:
            self.head.x = MAX_X

    def move_right(self):
        self.head.x += 1
        if self.head.x > MAX_X:
            self.head.x = 1


class Food():
    def __init__(self, window, char="x"):
        self.x = randint(1, MAX_X)
        self.y = randint(1, MAX_Y)
        self.char = char
        self.window = window

    def add(self):
        self.window.addstr(self.y, self.x, self.char)

    def reset(self):
        self.x = randint(1, MAX_X)
        self.y = randint(1, MAX_Y)


class Body():
    def __init__(self, x, y, char="~"):
        self.x = x
        self.y = y
        self.char = char

    @property
    def coor(self):
        return self.x, self.y



def main():
    curses.initscr()  # Initialize curses in Terminal window
    window = curses.newwin(HEIGHT, WIDTH, 0, 0)  # Create new window with given size
    window.timeout(SPEED)
    window.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    window.border(0)

    # Adding snake and food to window
    snake = Snake(SNAKE_X, SNAKE_Y, window)
    food = Food(window)

    while True:
        window.clear()
        window.border(0)
        food.add()
        snake.add()
        window.addstr(0, 50, snake.score)
        keypressed = window.getch()


        if keypressed == 113 or keypressed == 27:
            break

        if keypressed in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
            snake.new_direction(keypressed)

        if snake.head.x == food.x and snake.head.y == food.y:
            curses.flash()
            # curses.beep()
            snake.eat(food)

        snake.update()

        if snake.collided:
            break

    curses.endwin()
    return snake.hit_score


if __name__ == "__main__":
    main()
