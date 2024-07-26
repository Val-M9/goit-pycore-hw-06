from record import Record
from address_book import AddressBook


def main():
  book = AddressBook()
  rec1 = Record('Val')
  rec2 = Record('John')
  rec1.add_phone('12345679')
  rec1.add_phone('1111111111')
  rec2.add_phone('1234567590')
  rec2.add_phone('2222222222')
  book.add_record(rec1)
  book.add_record(rec2)

  for record in book.data.values():
    print(record)

  book.find_record('Val')
  rec1.find_phone('1111111111')
  book.delete('Val')
  rec2.edit_phone('1234567590', '3333333333')
  rec2.remove_phone('2222222222')

  for record in book.data.values():
    print(record)


if __name__ == '__main__':
  main()
