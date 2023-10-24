import kandinsky

""""""
class Data:
  width: int = 320
  height: int = 200
  fps: int = 30

""""""
class Image:
  
  """"""
  def __init__(self,
      pixels: list[list[list[int]]],
      x: int,
      y: int,
      is_drawing: bool = False
      ):
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

  """"""
  def draw(self):
    # Do not draw if is_drawing is False
    if not self.is_drawing:
      return
    # Set each pixel in array
    for y in range(0, len(self.pixels)):
      for x in range(0, len(self.pixels[y])):
        print(x,y,self.pixels[y][x])
        pixel = kandinsky.color(self.pixels[y][x])
        kandinsky.set_pixel(x, y, pixel)

  """"""
  def center(self):
    # Set x and y to center
    self.x = Data.width // 2 - self.width // 2
    self.y = Data.height // 2 - self.height // 2

""""""
class Screen:

  """"""
  def __init__(self,
      images: list[Image] = [],
      is_drawing: bool = False
      ):
    # Assign values
    self.images = images
    self.is_drawing = is_drawing

  """"""
  def draw(self):
    # Do not draw if is_drawing is False
    if not self.is_drawing:
      return
    # Draw each image in images array
    for image in self.images:
      image.draw()

  """"""
  def add_image(self,
      image: Image
      ):
    # Add image to images array
    self.images.append(image)

  """"""
  def remove_image(self,
      image: Image
      ):
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
