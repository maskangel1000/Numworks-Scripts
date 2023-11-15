import random

class Card:
  
  def __init__(self, value=None, suit=None):
    self.value = value
    self.suit = suit
    if self.value == None:
      self.value = Card.generate_random_value()
    if self.suit == None:
      self.suit = Card.generate_random_suit()
  
  @staticmethod
  def generate_random_value():
    return random.randint(1, 13)
  
  @staticmethod
  def generate_random_suit():
    return random.choice(["Spades", "Clubs", "Hearts", "Diamonds"])

  def __str__(self):
    value = self.value
    if self.value == 11:
      value = "Jack"
    elif self.value == 12:
      value = "Queen"
    elif self.value == 13:
      value = "King"
    return str(str(value) + " of " + self.suit)
    
class Game:
  
  def __init__(self, deck=None):
    print("assigning deck")
    self.deck = deck
    if self.deck == None:
      print("deck is none, generating deck")
      self.deck = Game.generate_random_deck()
      print("random deck generated")
  
  @staticmethod
  def generate_random_deck():
    deck = []
    for i in range(52):
      print("generating new card")
      new_card = Card()
      unique = True
      print("deck length:", len(deck))
      for card in deck:
        print("card:", card)
        print("card values:", card.value, new_card.value)
        print("card suits:", card.suit, new_card.suit)
        if card.value == new_card.value and card.suit == new_card.suit:
          print("not unique")
          unique = False
      while not unique:
        print("going through not unique loop")
        # print(3)
        new_card = Card()
        unique = True
        for card in deck:
        #   print(4)
          if card.value == new_card.value and card.suit == new_card.suit:
            unique = False
      deck.append(new_card)
    return deck
    
  def print_deck(self):
    for card in self.deck:
        print(card, end="\n")
  
  def get_top_card(self):
      return self.deck.pop()

print("creating game...")
game = Game()
print("printing deck...")
game.print_deck()
print("printing top card...")
print(game.get_top_card())
