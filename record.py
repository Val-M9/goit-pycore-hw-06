from fields import Name, Phone


class Record:
  def __init__(self, name):
    self.name = Name(name)
    self.phones: list[Phone] = []

  def add_phone(self, phone: str) -> None:
    try:
      valid_phone = Phone(phone).validate_phone()
      self.phones.append(valid_phone)
    except ValueError as e:
      print(e)

  def remove_phone(self, phone: str) -> None:
    if not phone in self.phones:
      print(f'Phone number {phone} was not found')
    self.phones.remove(phone)
    print(f'Phone number {phone} has been removed')

  def edit_phone(self, phone: str, new_phone: str) -> None:
    if not phone in self.phones:
      print(f'Phone number {phone} was not found')
    for i, phone_record in enumerate(self.phones):
      if phone_record == phone:
        self.phones[i] = new_phone
        print(f'Phone number {phone} has been changed to {new_phone}')

  def find_phone(self, phone: str) -> None:
    if not phone in self.phones:
      print(f'Phone number {phone} was not found')
    for phone_record in self.phones:
      if phone_record == phone:
        print(f'Phone number {phone} was found')

  def __str__(self):
    return f'Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}'
