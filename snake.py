class Point:
    row = 0
    col = 0

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def copy(self):
        return Point(row=self.row, col=self.col)

import pygame
import random

pygame.init()
W = 1000
H = 800

ROW = 30
COL = 40

size = (W, H)
window = pygame.display.set_mode(size)
pygame.display.set_caption('贪吃蛇beta')

bg_color = (255, 255, 255)
snake_color = (200, 200, 200)

head = Point(row=int(ROW / 2), col=int(COL / 2))
head_color = (0, 128, 128)

snakes = [
    Point(row=head.row, col=head.col + 1),
    Point(row=head.row, col=head.col + 2),
    Point(row=head.row, col=head.col + 3),
    Point(row=head.row, col=head.col + 4)
]


def get_food():
    while 1:
        pos = Point(row=random.randint(0, ROW - 1), col=random.randint(0, COL - 1))

        is_coll = False

        if head.row == pos.row or head.col == pos.col:
            is_coll = True

        for snake in snakes:
            if snake.row == pos.row or snake.col == pos.col:
                is_coll = True
                break

        if not is_coll:
            break

    return pos


food = get_food()
food_color = (10, 10, 10)


def rect(point, color):
    cell_width = W / COL
    cell_height = H / ROW

    left = point.col * cell_width
    top = point.row * cell_height

    pygame.draw.rect(
        window, color,
        (left, top, cell_width, cell_height)
    )
    pass


direct = "left"

quit = True
clock = pygame.time.Clock()

while quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 119:
                if direct == "left" or direct == "right":
                    direct = "up"
            if event.key == 115:
                if direct == "left" or direct == "right":
                    direct = "down"
            if event.key == 97:
                if direct == "up" or direct == "down":
                    direct = "left"
            if event.key == 100:
                if direct == "up" or direct == "down":
                    direct = "right"

    eat = (head.row == food.row and head.col == food.col)

    if eat:
        food = get_food()

    snakes.insert(0, head.copy())

    if not eat:
        snakes.pop()

    if direct == "up":
        head.row -= 1
    if direct == "down":
        head.row += 1
    if direct == "left":
        head.col -= 1
    if direct == "right":
        head.col += 1

    dead = False

    if head.col < 0 or head.row < 0 or head.col >= COL or head.row >= ROW:
        dead = True

    for snake in snakes:
        if head.col == snake.col and head.row == snake.row:
            dead = True

    if dead == True:
        print("你死得好惨啊")
        quit = False

    pygame.draw.rect(window, bg_color, (0, 0, W, H))
    for snake in snakes:
        rect(snake, snake_color)
    rect(head, head_color)
    rect(food, food_color)

    pygame.display.flip()

    clock.tick(20)



