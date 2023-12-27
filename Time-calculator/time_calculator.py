def add_time(start, duration, day=None):
  # Parse la hora de inicio
  start_time, period = start.split()
  start_hour, start_minute = map(int, start_time.split(':'))

  # Parse la duración
  duration_hour, duration_minute = map(int, duration.split(':'))

  # Convertir la hora de inicio a formato de 24 horas
  if period == 'PM' and start_hour != 12:
      start_hour += 12

  # Calcular el total de minutos
  total_start_minutes = start_hour * 60 + start_minute
  total_duration_minutes = duration_hour * 60 + duration_minute

  # Calcular la suma de los minutos iniciales y la duración
  total_minutes = total_start_minutes + total_duration_minutes

  # Calcular la nueva hora en formato de 24 horas
  new_hour = total_minutes // 60 % 24
  new_minute = total_minutes % 60

  # Calcular los días adicionales
  days_later = total_minutes // (24 * 60)

  # Calcular el nuevo día de la semana si se proporciona
  if day:
      day = day.lower().capitalize()
      days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
      day_index = days_of_week.index(day)
      new_day_index = (day_index + days_later) % 7
      new_day = f", {days_of_week[new_day_index]}"
  else:
      new_day = ""

  # Determinar el período (AM o PM)
  new_period = 'AM' if new_hour < 12 else 'PM'

  # Convertir a 12 horas
  if new_hour > 12:
      new_hour -= 12
  elif new_hour == 0:
      new_hour = 12

  # Construir el resultado
  if days_later == 1:
      days_later_str = "(next day)"
  elif days_later > 1:
      days_later_str = f"({days_later} days later)"
  else:
      days_later_str = ""

  result = f"{new_hour}:{new_minute:02} {new_period}{new_day} {days_later_str}".strip()
  return result
