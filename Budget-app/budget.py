def truncate(asgh):
  multiplier = 10
  return int(asgh * multiplier) / multiplier


def getTotals(categorias):
  total = 0
  breakdown = []
  for category in categorias:
    total += category.get_withdrawls()
    breakdown.append(category.get_withdrawls())
  rounded = list(map(lambda x: truncate(x / total), breakdown))
  return rounded


'''
entonces con 
lambda x: truncate(x / total): Definimos una función anónima (lambda) que toma un argumento x y devuelve el resultado de la operación truncate(x / total). La función lambda toma cada elemento x de la lista breakdown y realiza la operación especificada.

Con map(función, iterable): Aplicamos  la función especificada a cada elemento del iterable. En este caso, la función es la lambda definida anteriormente, y el iterable es la lista breakdown.

list(...): Convierte el resultado de map de nuevo en una lista.    Todo es posible, si pueds imaginarlo puedes hacerlo cueste lo que cueste
'''


def create_spend_chart(categoriass):
  res = "Percentage spent by category\n"
  i = 100
  totals = getTotals(categoriass)
  while i >= 0:
    cat_spaces = " "
    for total in totals:
      if total * 100 >= i:
        cat_spaces += "o  "
      else:
        cat_spaces += "   "  # Cambiado de un solo espacio a tres espacios
    res += str(i).rjust(3) + "|" + cat_spaces + ("\n")
    i -= 10

  dashes = "-" + "---" * len(categoriass)
  names = []
  x_axis = ""
  for category in categoriass:
    names.append(category.name)

  maxi = max(names, key=len)

  for x in range(len(maxi)):
    nameStr = '     '
    for name in names:
      if x >= len(name):
        nameStr += "   "
      else:
        nameStr += name[x] + "  "  # Cambiado de un solo espacio a dos espacios
    if (x != len(maxi) - 1):
      nameStr += '\n'

    x_axis += nameStr

  res += dashes.rjust(len(dashes) + 4) + '\n' + x_axis
  return res


class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = list()

  def __str__(self):
    title = f"{self.name:*^30}\n"
    items = ""
    total = 0
    for item in self.ledger:  # representacion
      items += f"{item['description'][0:23]:23}" + f"{item['amount']: >7.2f}" + '\n'
      total += item['amount']

    output = title + items + "Total: " + str(total)
    return output

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if (self.check_funds(amount)):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  def get_balance(self):
    total_cash = 0
    for item in self.ledger:
      total_cash += item["amount"]

    return total_cash

  def transfer(self, amount, category):
    if (self.check_funds(amount)):
      self.withdraw(amount, "Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)
      return True
    return False

  def check_funds(self, amount):
    if (self.get_balance() >= amount):
      return True
    return False

  def get_withdrawls(self):
    total = 0
    for item in self.ledger:
      if item["amount"] < 0:
        total += item["amount"]
    return total
