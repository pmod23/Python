


class Person:
    def __init__(self, first, last, phone_number):
        self.first = first
        self.last = last
        self.phone_number = phone_number

#finding a name by full name
    def full_name(self):
        return f'{self.first} {self.last}'

#returning a string of class Person
    def __str__(self):
        return f"{self.first} {self.last} : {self.phone_number}"

#starting with empty list to store contacts
contacts = list()

users_input = ""


print("Welcome to the address book program")

#while loop to go on until user decides to "Quit" the program
while users_input != "q":
    print("Available options")
    print("1 - Enter a contact")
    print("2 - Display contacts")
    print("3 - Find contact")
    print("q - quit program")
    users_input = input("Select option: ")
#logic
    if users_input == "1":
        print("Enter your contact's information")

        first_name = input("First name = ")
        last_name = input("Last name = ")
        phone_number = input("Phone number = ")

        our_contact = Person(first_name, last_name, phone_number)
        contacts.append(our_contact)
        print("Thank you we have received your contacts information")
#loop through contacts list to see all contacts
    elif users_input == "2":
        for contact in contacts:
            print(contact)
        input("Contacts displayed. Hit enter to continue.")
    elif users_input == "3":
        to_lookup = input("Enter contact's name to lookup\n")
        for contact in contacts:
            if to_lookup in contact.full_name():
                print(contact)
    elif users_input.lower() == "q":
        break


print("Thank you for using the address book")
