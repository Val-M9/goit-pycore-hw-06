from collections import UserDict
from record import Record


class AddressBook(UserDict):
  def add_record(self, record: Record):
    self.data[record.name] = record

  def find_record(self, name: str) -> None:
    for record_name in self.data.keys():
      if str(record_name) == name:
        print(f'{self.data[record_name]} was found')
        break
    else:
      print(f'Contact {name} was not found')

  def delete(self, name: str) -> None:
    for record_name in self.data.keys():
      if str(record_name) == name:
        self.data.pop(record_name)
        print(f'Contact {name} has been deleted')
        break
    else:
      print(f'Contact {name} was not found')
