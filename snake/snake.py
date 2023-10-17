from kandinsky import *
from ion import *
from time import *
from random import *

WIDTH = 320
HEIGHT = 225

BOARD_WIDTH = 10
BOARD_HEIGHT = 10

BG_COLOR = color(255, 255, 255)
TEXT_COLOR = color(0, 0, 0)

SECONDS_PER_MOVE = 0.2
SNAKE_COLOR = color(30, 200, 0)
SNAKE_HEAD_COLOR = color(90, 170, 0)

APPLE_COLOR = color(200, 30, 0)

won = None
score = 0

def check_win() -> None:
  new_locations = []
  for location in snake_locations:
    new_locations.append(location)
  for location in snake_locations:
    new_locations.pop(0)
    for new_location in new_locations:
      if location[0] == new_location[0] and location[1] == new_location[1]:
        return False
    if location[0] >= BOARD_WIDTH or location[1] >= BOARD_HEIGHT:
      return False
    if location[0] < 0 or location[1] < 0:
      return False
  if len(snake_locations) > BOARD_WIDTH*BOARD_HEIGHT - 1:
    return True
  return None

def set_apple_location() -> None:
  global apple_location
  apple_location = (randint(0, BOARD_WIDTH-1), randint(0, BOARD_HEIGHT-1))
  while True:
    for location in snake_locations:
      if apple_location[0] == location[0] and apple_location[1] == location[1]:
        apple_location = (randint(0, BOARD_WIDTH-1), randint(0, BOARD_HEIGHT-1))
        break
    else:
      break

def set_direction() -> None:
  global snake_direction_queue, paused
  if paused:
    if keydown(KEY_PLUS):
      paused = False
    else:
      return
  if keydown(KEY_RIGHT):
    if snake_direction != "left":
      snake_direction_queue = "right"
  if keydown(KEY_LEFT):
    if snake_direction != "right":
      snake_direction_queue = "left"
  if keydown(KEY_UP):
    if snake_direction != "down":
      snake_direction_queue = "up"
  if keydown(KEY_DOWN):
    if snake_direction != "up":
      snake_direction_queue = "down"
  if keydown(KEY_MINUS):
    paused = True
    draw()
    
def move() -> None:
  global eating_apple, snake_locations, apple_location, score, snake_direction
  if snake_direction_queue == "right":
    snake_direction = "right"
    snake_x = snake_locations[-1][0]+1
    snake_y = snake_locations[-1][1]
  elif snake_direction_queue == "left":
    snake_direction = "left"
    snake_x = snake_locations[-1][0]-1
    snake_y = snake_locations[-1][1]
  elif snake_direction_queue == "up":
    snake_direction = "up"
    snake_x = snake_locations[-1][0]
    snake_y = snake_locations[-1][1]-1
  elif snake_direction_queue == "down":
    snake_direction = "down"
    snake_x = snake_locations[-1][0]
    snake_y = snake_locations[-1][1]+1
  snake_locations.append((snake_x, snake_y))
  for location in snake_locations:
    if location[0] == apple_location[0] and location[1] == apple_location[1] and not eating_apple:
      eating_apple = True
      score += 1
      set_apple_location()
  if not eating_apple:
    snake_locations.pop(0)
  eating_apple = False
    
def draw(win: bool = False) -> None:
  global won
  for y in range(0, BOARD_HEIGHT):
    for x in range(0, BOARD_WIDTH):
      for location in snake_locations:
        if location[0] == x and location[1] == y:
          break
      else:
        if apple_location[0] != x or apple_location[1] != y:
          fill_rect(x*WIDTH//BOARD_WIDTH, y*HEIGHT//BOARD_HEIGHT, WIDTH//BOARD_WIDTH, HEIGHT//BOARD_HEIGHT, BG_COLOR)
          
  win = check_win()
  if win is True:
    won = True
  elif win is False:
    won = False
  if won is True:
    draw_string("You won!\nScore: " + str(score), 0, 0, TEXT_COLOR, BG_COLOR)
    return
  elif won is False:
    draw_string("You lost!\nScore: " + str(score), 0, 0, TEXT_COLOR, BG_COLOR)
    return
  apple_x = apple_location[0]*WIDTH//BOARD_WIDTH
  apple_y = apple_location[1]*HEIGHT//BOARD_HEIGHT
  apple_width = WIDTH//BOARD_WIDTH
  apple_height = HEIGHT//BOARD_HEIGHT
  fill_rect(apple_x, apple_y, apple_width, apple_height, APPLE_COLOR)
  for idx, location in enumerate(snake_locations):
    snake_x = location[0]*WIDTH//BOARD_WIDTH
    snake_y = location[1]*HEIGHT//BOARD_HEIGHT
    snake_width = WIDTH//BOARD_WIDTH
    snake_height = HEIGHT//BOARD_HEIGHT
    if idx == len(snake_locations)-1:
      fill_rect(snake_x, snake_y, snake_width, snake_height, SNAKE_HEAD_COLOR)
    else:
      fill_rect(snake_x, snake_y, snake_width, snake_height, SNAKE_COLOR)
  if paused:
    draw_string("Paused", WIDTH//2-40, HEIGHT//2-20, TEXT_COLOR, BG_COLOR)
    draw_string("Press + to resume", WIDTH//2-80, HEIGHT//2, TEXT_COLOR, BG_COLOR)

last_time = monotonic()
eating_apple = False
paused = False
snake_direction = "right"
snake_direction_queue = "right"
snake_locations = [(0, 0)]
set_apple_location()
draw()
while True:
  set_direction()
  if not paused:
    # draw_string(snake_direction,100,0)
    # draw_string(snake_direction_queue,100,20)
    new_time = monotonic()
    if new_time - last_time > SECONDS_PER_MOVE and won is None:
      last_time = new_time
      new_time = monotonic()
      move()
      draw()
