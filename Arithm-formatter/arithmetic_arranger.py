def arithmetic_arranger(problems, show_answer=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  arranged_problems = {
      "Primera_linea": "",
      "Segunda_linea": "",
      "dash_l": "",
      "answ_l": ""
  }

  for problem in problems:
    operand1, operator, operand2 = problem.split()

    if operator not in ["+", "-"]:
      return "Error: Operator must be '+' or '-'."

    if not operand1.isdigit() or not operand2.isdigit():
      return "Error: Numbers must only contain digits."

    if len(operand1) > 4 or len(operand2) > 4:
      return "Error: Numbers cannot be more than four digits."

    width = max(len(operand1), len(operand2)) + 2
    arranged_problems["Primera_linea"] += operand1.rjust(width) + "    "
    arranged_problems["Segunda_linea"] += operator + " " + operand2.rjust(
        width - 2) + "    "
    arranged_problems["dash_l"] += "-" * width + "    "

    if show_answer:
      if operator == "+":
        answer = str(int(operand1) + int(operand2))
      else:
        answer = str(int(operand1) - int(operand2))

      arranged_problems["answ_l"] += answer.rjust(width) + "    "

  arranged_output = arranged_problems["Primera_linea"].rstrip() + "\n"
  arranged_output += arranged_problems["Segunda_linea"].rstrip() + "\n"
  arranged_output += arranged_problems["dash_l"].rstrip()

  if show_answer:
    arranged_output += "\n" + arranged_problems["answ_l"].rstrip()

  return arranged_output
