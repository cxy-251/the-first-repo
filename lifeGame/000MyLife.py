import sys

import pygame
from pygame.constants import K_s, QUIT, KEYDOWN

pygame.init()

SCR_RECT = pygame.Rect(0, 0, 900, 600)
screen = pygame.display.set_mode(SCR_RECT.size)

pygame.display.set_caption("1234")

font = pygame.font.SysFont("cardamon", 18)

DEAD, ALIVE, MARKED, NON_MARKED, NEW_ALIVE, DIED_OUT = 0, 1, 2, 3, 4, 5
CELL_SIZE = 10
HEIGHT, WIDTH = SCR_RECT.height // CELL_SIZE, SCR_RECT.width // CELL_SIZE
COL_0, ROW_0 = 14, 1


cursor = [(COL_0 + WIDTH) // 2, HEIGHT // 2]


clock = pygame.time.Clock()

WALL_COLOR = (0xff, 0xff, 0xff)
for y in range(HEIGHT):
    pygame.draw.rect(screen, WALL_COLOR, pygame.Rect(0, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, WALL_COLOR, pygame.Rect((WIDTH - 1) * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
for x in range(WIDTH):
    pygame.draw.rect(screen, WALL_COLOR, pygame.Rect(x * CELL_SIZE, 0, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, WALL_COLOR, pygame.Rect(x * CELL_SIZE, (HEIGHT - 1) * CELL_SIZE, CELL_SIZE, CELL_SIZE))


# fresh = (0xff, 0xe5, 0xcc)
# pink = (0xff, 0x99, 0xcc)
# black = (0x22, 0x22, 0x22)
# grey = (0x55, 0x55, 0x55)
# yellow = (0xff, 0xff, 0x99)
# light_black = (0x33, 0x33, 0x33)
# NEW_ALIVE_COLOR, DIED_OUT_COLOR, ALIVE_COLOR, MARKED_COLOR, DEAD_COLOR, _\
#     = fresh, pink, black, grey, yellow, light_black

blue = (0x00, 0x00, 0xff)
pink = (0xff, 0x99, 0xcc)
white = (0xee, 0xee, 0xee)
dim_blue = (0x66, 0xb2, 0xff)
blue_purple = (0xb2, 0x66, 0xff)
light_grey = (0xe0, 0xe0, 0xe0)
NEW_ALIVE_COLOR, DIED_OUT_COLOR, ALIVE_COLOR, MARKED_COLOR, DEAD_COLOR, c6\
    = blue, pink, white, dim_blue, blue_purple, light_grey

# light_red = (0xff, 0x66, 0x66)
# pure_yh = (0xff, 0xff, 0x00)
# dim_blue = (0x66, 0xb2, 0xff)
# light_green = (0x00, 0xcc, 0x66)
# pure_wh = (0xff, 0xff, 0xff)
# light_grey = (0xe0, 0xe0, 0xe0)
# NEW_ALIVE_COLOR, DIED_OUT_COLOR, ALIVE_COLOR, MARKED_COLOR, DEAD_COLOR, c6\
#     = light_red, pure_yh, dim_blue, light_green, pure_wh, light_grey


black = (0x22, 0x22, 0x22)

CURSOR_COLOR = (0x00, 0x00, 0xff)
SIDE_COLOR = (200, 200, 200)
univ = [[DEAD for x in range(WIDTH)] for y in range(HEIGHT)]
hist = [[NON_MARKED for x in range(WIDTH)] for y in range(HEIGHT)]
grid = True
def draw(screen):
    for y in range(ROW_0, HEIGHT - 1):
        for x in range(COL_0, WIDTH - 1):
            if hist[y][x] == NEW_ALIVE:
                pygame.draw.rect(screen, NEW_ALIVE_COLOR, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

            elif hist[y][x] == DIED_OUT:
                pygame.draw.rect(screen, DIED_OUT_COLOR, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

            elif univ[y][x] == ALIVE:
                pygame.draw.rect(screen, ALIVE_COLOR, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

            elif hist[y][x] == MARKED:
                pygame.draw.rect(screen, MARKED_COLOR, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

            elif univ[y][x] == DEAD:
                pygame.draw.rect(screen, DEAD_COLOR, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

            if grid:
                pygame.draw.rect(screen, c6, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    pygame.draw.rect(screen, CURSOR_COLOR,
                     pygame.Rect(cursor[0] * CELL_SIZE, cursor[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    pygame.draw.rect(screen, SIDE_COLOR, pygame.Rect(10, 10, 130, 580))

    screen.blit(font.render("generation: %d" % generation, True, black), (20, 10))
    screen.blit(font.render("space : alive/dead", True, black), (20, 22))
    screen.blit(font.render("s : start/stop", True, black), (20, 34))
    screen.blit(font.render("n : next", True, black), (20, 46))
    screen.blit(font.render("r : random", True, black), (20, 58))
    screen.blit(font.render("p : pattern", True, black), (20, 70))
    screen.blit(font.render("g : grid", True, black), (20, 94))
    screen.blit(font.render("q : quit", True, black), (20, 106))


def countAliveCells(x, y):
    sum = 0
    sum += univ[y - 1][x - 1]
    sum += univ[y - 1][x]
    sum += univ[y - 1][x + 1]
    sum += univ[y][x - 1]
    sum += univ[y][x + 1]
    sum += univ[y + 1][x - 1]
    sum += univ[y + 1][x]
    sum += univ[y + 1][x + 1]
    return sum


generation = 0
def next(univ, hist, generation):
    next_field = [[False for x in range(WIDTH)] for y in range(HEIGHT)]
    for y in range(ROW_0, HEIGHT - 1):
        for x in range(COL_0, WIDTH - 1):

            num_alive_cells = countAliveCells(x, y)
            if univ[y][x] == ALIVE or hist[y][x] == DIED_OUT:
                hist[y][x] = MARKED
            if num_alive_cells == 2:
                next_field[y][x] = univ[y][x]
            elif num_alive_cells == 3:
                if univ[y][x] == DEAD:
                    hist[y][x] = NEW_ALIVE
                next_field[y][x] = ALIVE
            else:
                if univ[y][x] == ALIVE:
                    hist[y][x] = DIED_OUT
                next_field[y][x] = DEAD

    univ = next_field
    generation += 1


running = False
def update():
    # if running:
    next(univ, hist, generation)


while True:
    clock.tick(60)
    update()
    draw(screen)
    pygame.display.update()

    # for event in pygame.event.get():
    #     if event.type == QUIT:
    #         pygame.quit()
    #         sys.exit()
    #     elif event.type == KEYDOWN:
    #         if event.key == K_s:
    #             running ^= 1






