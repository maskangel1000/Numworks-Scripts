import kandinsky

class Calculator:
  """A dataclass to store data for the calculator

  width : int = 320
    the width of the calculator screen
  height : int = 200
    the height of the calculator screen
  fps : int = 30
    the frames drawn to the screen per second
  """
  width: int = 320
  height: int = 200
  fps: int = 30

class Image:
  """A class to represent an image by an array of pixels

  Attributes
    pixels : list[list[list[int]]]
      2D array of [int, int, int] arrays representing the color of a pixel
    x : int
      The top left x coordinate of the image
    y : int
      The top left y coordinate of the image
    is_drawing : bool
      If the image should be drawn in the next frame
  """
  
  def __init__(self,
      pixels: list[list[list[int]]],
      x: int,
      y: int,
      is_drawing: bool = False
      ):
    """Constructs the Image object

    Parameters
      pixels : list[list[list[int]]]
        2D array of [int, int, int] arrays representing the color of a pixel
      x : int
        The top left x coordinate of the image
      y : int
        The top left y coordinate of the image
      is_drawing : bool = False
        If the image should be drawn in the next frame

    Raises
      TypeError
        If the image dimensions are not uniform
    """
        
    # Exception handling
    row_length = len(pixels[0])
    for row in pixels:
      if len(row) != row_length:
        raise TypeError("Image dimensions must be uniform")
      row_length = len(row)

    # Assign values
    self.pixels = pixels
    self.width = len(pixels[0])
    self.height = len(pixels)
    self.is_drawing = is_drawing

  def draw(self) -> None:
    """Draws the image to the screen if is_drawing is True"""
    # Do not draw if is_drawing is False
    if not self.is_drawing:
      return
    # Set each pixel in array
    for y in range(0, len(self.pixels)):
      for x in range(0, len(self.pixels[y])):
        print(x,y,self.pixels[y][x])
        pixel = kandinsky.color(self.pixels[y][x])
        kandinsky.set_pixel(x, y, pixel)

  def center(self) -> None:
    """Moves the x and y of the image to the center of the screen"""
    # Set x and y to center
    self.x = Calculator.width // 2 - self.width // 2
    self.y = Calculator.height // 2 - self.height // 2

class Screen:
  """A class to represent what is drawn to the screen

  Attributes
    images : list[Image]
      An array of the images that are drawn to the screen
    is_drawing : bool
      If the images should be drawn in the next frame
  """
  def __init__(self,
      images: list[Image] = [],
      is_drawing: bool = False
      ):
    """Constructs a Screen object

    Parameters
      images : list[Image] = []
        An array of the images that are drawn to the screen
      is_drawing : bool = False
        If the images should be drawn in the next frame
    """
    # Assign values
    self.images = images
    self.is_drawing = is_drawing

  def draw(self) -> None:
    """Draws the images to the screen if is_drawing is True"""
    # Do not draw if is_drawing is False
    if not self.is_drawing:
      return
    # Draw each image in images array
    for image in self.images:
      image.draw()

  def add_image(self,
      image: Image
      ) -> None:
    """Adds an Image object to the images array

    Parameters
      image
        The Image object to be added to the images array
    """
    # Add image to images array
    self.images.append(image)

  def remove_image(self,
      image: Image
      ) -> None:
    """Removes an Image object from the images array

    Parameters
      image
        The Image object to be removed from the images array
    """
    # Check for image in images array
    for idx, img in enumerate(this.images):
      if img is image:
        self.images.remove([idx])


screen = Screen(is_drawing=True)
img1 = Image([[[0, 0, 0] for a in range(0, 10)] for b in range(0, 10)], 0, 0, True)
img1.center()
print(img1.pixels)
screen.add_image(img1)
# while True:
#   screen.draw()
