import kandinsky
import ion
import time

WIDTH = 320
HEIGHT = 222
FPS = 30

BG_COLOR = kandinsky.color(0, 0, 0)
PLAYER_COLOR = kandinsky.color(0, 255, 0)
COMP_COLOR = kandinsky.color(255, 0, 0)
BALL_COLOR = kandinsky.color(255, 255, 255)

PONG_WIDTH = 10
PONG_HEIGHT = 40
BALL_WIDTH = 10
BALL_HEIGHT = 10

BALL_PIXELS_PER_FRAME = 7
PONG_PIXELS_PER_FRAME = 5

player_y = HEIGHT//2-PONG_HEIGHT//2
comp_y = player_y

ball_x = WIDTH//2-BALL_WIDTH//2
ball_y = HEIGHT//2-BALL_HEIGHT//2
ball_direction = "left"

def set_ball_direction():
  global ball_direction
  # Check player collision
  if (ball_x - BALL_WIDTH//2 < 0 + PONG_WIDTH - 5):
    if (ball_y >= player_y and ball_y <= player_y + PONG_HEIGHT):
      ball_direction = "right"
      print(ball_y, "-", BALL_HEIGHT//2, ">=", player_y, "-", PONG_HEIGHT//2)
  # Check comp collision
  if (ball_x + BALL_WIDTH//2 > WIDTH - PONG_WIDTH - 5):
    if (ball_y >= comp_y and ball_y <= comp_y + PONG_HEIGHT):
      ball_direction = "left"

def draw_background():
  kandinsky.fill_rect(0, 0, WIDTH, HEIGHT, BG_COLOR)

def draw_pongs():
  global player_y
  # Draw player pong
  kandinsky.fill_rect(0, player_y, PONG_WIDTH, PONG_HEIGHT, PLAYER_COLOR)
  # Draw comp pong
  kandinsky.fill_rect(WIDTH-PONG_WIDTH, comp_y, PONG_WIDTH, PONG_HEIGHT, COMP_COLOR)
  # Check movement
  if ion.keydown(ion.KEY_UP):
    if player_y >= 0:
      player_y -= PONG_PIXELS_PER_FRAME
  elif ion.keydown(ion.KEY_DOWN):
    if player_y + PONG_HEIGHT <= HEIGHT:
      player_y += PONG_PIXELS_PER_FRAME
  
def draw_ball():
  global ball_x, ball_y
  kandinsky.fill_rect(ball_x, ball_y, BALL_WIDTH, BALL_HEIGHT, BALL_COLOR)
  set_ball_direction()
  if ball_direction == "right":
    ball_x += BALL_PIXELS_PER_FRAME
  else:
    ball_x -= BALL_PIXELS_PER_FRAME

def draw():
  draw_background()
  draw_ball()
  draw_pongs()

old_time = time.monotonic()
while True:
 new_time = time.monotonic()
 if new_time - old_time >= 1/FPS:
   old_time = new_time
   draw()
