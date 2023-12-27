class Rectangle:

  def __init__(self, width,
               height):  # especificamos los atributos de alto / ancho
    self.width = width
    self.height = height

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'

  #arrancamos con los metodos
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width**2 + self.height**2)**0.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    string = (("*" * self.width) + "\n") * self.height
    return string

  def get_amount_inside(self, shape):
    return int(self.get_area() / shape.get_area())


#creamos otra clase cuadrado que heeredara los atributos y metodos de Rectangulo
class Square(Rectangle):

  def __init__(self, side):
    super().__init__(side, side)

  def __str__(self):
    return f'Square(side={self.width})'

  def set_side(self, side):
    self.set_width(side)
    self.set_height(side)
