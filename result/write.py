import addressbook_pb2

address_book = addressbook_pb2.AddressBook()
person = address_book.people.add()
person.id = int(raw_input("Enter person ID number: "))
person.name = raw_input("Enter name: ")
email = raw_input("Enter email address (blank for none): ")
if email != "":
  person.email = email
while True:
  number = raw_input("Enter a phone number (or leave blank to finish): ")
  if number == "":
    break
  phone_number = person.phones.add()
  phone_number.number = number
  type = raw_input("Is this a mobile, home, or work phone? ")
  if type == "mobile":
    phone_number.type = addressbook_pb2.Person.MOBILE
  elif type == "home":
    phone_number.type = addressbook_pb2.Person.HOME
  elif type == "work":
    phone_number.type = addressbook_pb2.Person.WORK
  else:
    print("Unknown phone type; leaving as default value.")

with open(sys.argv[1], "wb") as f:
  f.write(address_book.SerializeToString())