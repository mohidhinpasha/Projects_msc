from datetime import date

def is_valid_date(text):
  """determines whether the input string in the format mm/dd/yyyy is a valid date."""
  try:
    month, day, year = map(int, text.split('/'))
    return 1 <= month <= 12 and 1 <= day <= 31 and year > 0  # Check if month, day, and year are within valid ranges
  except (ValueError, IndexError):
    return False

def calculate_age(birthdate):
  """determines the user's age by using their birthdate and the current date."""
  today = date.today()
  age = today.year - birthdate.year
  # Verify whether this year's birthday has passed.
  if (birthdate.month, birthdate.day) > (today.month, today.day):
    age -= 1
  return age

while True:
  try:
    birth_str = input("Enter your date of birth (mm/dd/yyyy): ")
    if is_valid_date(birth_str):
      month, day, year = map(int, birth_str.split('/'))
      birthdate = date(year, month, day)  # Create date object
      age = calculate_age(birthdate)
      #European format date format
      european_date = birthdate.strftime("%d/%m/%Y")
      print(f"Your age is {age}. (Date of Birth in European format: {european_date})")
      break
    else:
      print("Invalid date format. Please try again in mm/dd/yyyy format.")
  except ValueError:
    print("Invalid date format. Please try again in mm/dd/yyyy format.")