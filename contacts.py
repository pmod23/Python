from peewee import *


db = SqliteDatabase('people.db')

db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Person(BaseModel):
    first_name = CharField()
    last_name = CharField()
    phone_number = CharField()

    class Meta:
        database = db


db.create_tables([Person])

users_input = ""


print("Welcome to the address book program")

while users_input != "q":
    print("Available options")
    print("1 - Enter a contact")
    print("2 - Display contacts")
    print("3 - Find contact")
    print("q - quit program")
    users_input = input("Select option: ")

    if users_input == "1":
        print("Enter your contact's information")

        first = input("First name = ")
        last = input("Last name = ")
        phone = input("Phone number = ")

        our_contact = Person(
            first_name=first, last_name=last, phone_number=phone)
        our_contact.save()
        print("Thank you we have received your contacts information")
    elif users_input == "2":
        for contact in Person.select():
            print("{} {} : {}".format(contact.first_name,
                                      contact.last_name, contact.phone_number))
        input("Contacts displayed. Hit enter to continue.")
    elif users_input == "3":
        to_lookup = input("Enter contact's name to lookup\n").lower()
        found = False
        for contact in Person.select():
            if to_lookup.lower() in contact.first_name.lower():
                print(contact.first_name, contact.last_name, contact.phone_number)
                found = True

        if found == False:
            print("Contact not found.")

    elif users_input.lower() == "q":
        break
