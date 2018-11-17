import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random import randint

# General Variables

bredde = 35
hoyde = 20
max_x = bredde - 1
max_y = hoyde - 1
snake_lengde = 5
snake_x = snake_lengde + 1
snake_y = 3
timeout = 100

# Obj

"""Snake object"""

class Snake(object):
    class Snake(object):
        # 1  Add Opposite Direction Map
        OPP_DIR_MAP = {
            KEY_UP: KEY_DOWN, KEY_DOWN: KEY_UP,
            KEY_LEFT: KEY_RIGHT, KEY_RIGHT: KEY_LEFT,
        }

        # 2 def Init, set score to 0, set timeout, body list
        def __init__(self, x, y, window):
            self.body_list = []
            self.hit_score = 0
            self.timeout = timeout

        # 3 Make Properties on the objects,
        # which is a special decorator that modifies
        # the function. makes it so when you access the attribute,
        # it auto calls the function. Makes for more reusable code
        @property
        def score(self):
            return 'Score: {}'.format(self.hit_score)


    class Body(object):
        def __init__(self):
            self.x = 'this is the'

        def method_a(self, foo):
            print
            self.x + ' ' + foo

    body = Body().method_a('Body')

    class Food(object):
        def __init__(self):
            self.y = 'Yum, Tasty'

        def method_a(self, foo):
            print
            self.y + ' ' + foo

    food = Food().method_a('Food')