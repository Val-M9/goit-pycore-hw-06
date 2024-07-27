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
    super().__init__(value)
    self.validate_phone()
    self.value = value

  def validate_phone(self) -> str:
    match = re.match(r'\d{10}', self.value)
    if not match:
      raise ValueError(
          f'Phone number must contain digits. The length of the phone number must be 10 digits.')

  def __eq__(self, other: object) -> bool:
    if isinstance(other, Phone):
      return self.value == other.value
    if isinstance(other, str):
      return self.value == other
    return False
