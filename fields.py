import re


class Field:
  def __init__(self, value):
    self.value = value

  def __str__(self):
    return str(self.value)


class Name(Field):
  def __init__(self, value: str):
    self.value = value


class Phone(Field):
  def __init__(self, value: str):
    self.value = value

  def validate_phone(self) -> str:
    match = re.match(r'\d{10}', self.value)
    if not match:
      raise ValueError(
          f'Phone number must contain digits. The length of the phone number must be 10 digits.')
    return self.value
