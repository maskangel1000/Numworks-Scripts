import kandinsky
import ion
import time

# Screen constants
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 222

# Color constants
BG_COLOR = kandinsky.color(0, 0, 0)
PLAYER_COLOR = kandinsky.color(0, 255, 0)
COMP_COLOR = kandinsky.color(255, 0, 0)
BALL_COLOR = kandinsky.color(255, 255, 255)

# Size constants
PONG_WIDTH = 10
PONG_HEIGHT = 40
BALL_WIDTH = 10
BALL_HEIGHT = 10

# Speed constants (NOT VELOCITY)
BALL_SPEED_HORIZONTAL = 100 # (idk)
PONG_SPEED = 100 # (idk)

def draw(delta: float):
  pass

delta = 0
while True:
  time1 = time.monotonic()
  draw(delta)
  time2 = time.monotonic()
  delta = time2 - time1
