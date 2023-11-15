import kandinsky
import ion
import random

HEIGHT = 220

class Card:
  
  CARD_OUTSIDE_WIDTH = 50
  CARD_OUTSIDE_HEIGHT = 80
  CARD_OUTSIDE_COLOR = kandinsky.color(0, 0, 0)
  CARD_INSIDE_WIDTH = 40
  CARD_INSIDE_HEIGHT = 70
  CARD_INSIDE_COLOR = kandinsky.color(255, 255, 255)
  
  def __init__(self, value: int, suit: str):
    self.value = value
    self.suit = suit

  def __str__(self) -> str:
    return self.get_value_str() + " of " + self.suit

  def get_value_str(self) -> str:
    if self.value == 1:
      value = "A"
    elif self.value == 11:
      value = "J"
    elif self.value == 12:
      value = "Q"
    elif self.value == 13:
      value = "K"
    else:
      value = str(self.value)
    return value
  
  def draw(self, x: int, y: int, face_down: bool = False):
    kandinsky.fill_rect(x, y, Card.CARD_OUTSIDE_WIDTH, Card.CARD_OUTSIDE_HEIGHT, Card.CARD_OUTSIDE_COLOR)
    kandinsky.fill_rect(
      x + (Card.CARD_OUTSIDE_WIDTH-Card.CARD_INSIDE_WIDTH)//2,
      y + (Card.CARD_OUTSIDE_HEIGHT-Card.CARD_INSIDE_HEIGHT)//2,
      Card.CARD_INSIDE_WIDTH,
      Card.CARD_INSIDE_HEIGHT,
      Card.CARD_INSIDE_COLOR
    )
    if not face_down:
      if self.get_value_str() == "10":
        kandinsky.draw_string(self.get_value_str(), x+15, y+20, Card.CARD_OUTSIDE_COLOR)
      else:
        kandinsky.draw_string(self.get_value_str(), x+20, y+20, Card.CARD_OUTSIDE_COLOR)
      # kandinsky.draw_string(self.suit[0], x+20, y+Card.CARD_INSIDE_HEIGHT-30, Card.CARD_OUTSIDE_COLOR)

class Game:
  def __init__(self):
    self.deck = Game.generate_deck()
    self.player_hand = [self.remove_random_card(), self.remove_random_card()]
    self.dealer_hand = [self.remove_random_card(), self.remove_random_card()]

  @staticmethod
  def generate_deck():
    deck = []
    for value in range(1, 14):
      for suit in ["Hearts", "Diamonds", "Spades", "Clubs"]:
        deck.append(Card(value, suit))
    return deck

  def remove_random_card(self) -> Card:
    return self.deck.pop(random.randint(0, len(self.deck)-1))

  def hit_or_stay(self) -> bool:
    if Game.get_sum(self.dealer_hand) < 17:
      self.dealer_hand.append(self.remove_random_card())
      return True
    return False

  def hit(self) -> None:
    self.player_hand.append(self.remove_random_card())

  @staticmethod
  def get_sum(hand) -> int:
    sum = 0
    aces = 0
    for i in range(len(hand)):
      card = hand[i]
      if card.value == 1 and aces == 0:
        aces += 1
        sum += 11
      elif card.value == 11 or card.value == 12 or card.value == 13:
        sum += 10
      else:
        sum += card.value
    if sum > 21:
      sum = 0
      for i in range(len(hand)):
        card = hand[i]
        sum += card.value
    return sum

  def print_deck(self) -> None:
    for card in self.deck:
      print(card)

  def get_dealer_hand_str(self) -> None:
    string = ""
    for card in self.dealer_hand:
      string += str(card) + ", "
    return string

  def get_player_hand_str(self) -> None:
    string = ""
    for card in self.player_hand:
      string += str(card) + ", "
    return string

game = Game()
draw = True
win = None
face_up = False
while True:
  if draw:
    draw = False
    for idx, card in enumerate(game.dealer_hand):
      if idx == 0 and not face_up:
        card.draw((idx+1)*10 + Card.CARD_OUTSIDE_WIDTH*idx, 10, True)
      else:
        card.draw((idx+1)*10 + Card.CARD_OUTSIDE_WIDTH*idx, 10)
    for idx, card in enumerate(game.player_hand):
      card.draw((idx+1)*10 + Card.CARD_OUTSIDE_WIDTH*idx, HEIGHT-10-Card.CARD_OUTSIDE_HEIGHT)
  if ion.keydown(ion.KEY_DOWN):
    face_up = True
    if win is not None:
      continue
    draw = True
    while game.hit_or_stay():
      game.hit_or_stay()
    if Game.get_sum(game.dealer_hand) > 21:
      win = True
    elif Game.get_sum(game.dealer_hand) >= Game.get_sum(game.player_hand):
      win = False
  elif ion.keydown(ion.KEY_UP) and not hitting:
    hitting = True
    if win is not None:
      continue
    draw = True
    game.hit()
    if Game.get_sum(game.player_hand) > 21:
      win = False
  if not ion.keydown(ion.KEY_UP):
    hitting = False
  if not draw and win is not None:
    break

print(win)
