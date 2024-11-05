import sys
from functools import wraps
from addressbook import AddressBook 
from record import Record
from phone import Phone
from birthday import Birthday

# Decorator to handle input errors and return appropriate error messages
def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Wrong input, please use help to check the correct syntax"
        except IndexError:
            return "Please provide valid data."
        except TypeError:
            return "Please provide valid data."
        except KeyError:
            return "Please provide valid data."
    return inner

# Adds a new contact or updates an existing one
@input_error
def add_contact(args, book: AddressBook) -> str:
    name, phone = args
    record = book.find(name)
    message = "Contact updated."
    
    if not record:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    
    record.add_phone(phone)
    return message

# Shows all contacts in the address book
@input_error
def get_all_contacts(book: AddressBook) -> str:
    if book.data:
        return str(book)
    return "No contacts found."

# Retrieves phone numbers for a given contact name
@input_error
def get_phone(args, book: AddressBook) -> str:
    name = args[0]
    record = book.find(name)
    if record:
        return ', '.join(str(phone) for phone in record.phones)
    return "Contact not found."

# Changes a phone number for a contact
@input_error
def change_contact(args, book: AddressBook) -> str:

    name, old_phone, new_phone = args
    record = book.find(name)
    if record:
            record.edit_phone(old_phone, new_phone)
            return "Contact updated."
    return "Contact not found."

# Adds a birthday to an existing contact
@input_error
def add_birthday(args, book: AddressBook) -> str:
    name, birthday_str = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    
    record.add_birthday(birthday_str)
    return "Birthday added."

# Shows the birthday of a contact
@input_error
def show_birthday(args, book: AddressBook) -> str:
    name = args[0]
    record = book.find(name)
    
    if not record:
        return "Contact not found."
    
    if record and record.birthday:
        return f"{name}'s birthday is on {record.birthday.value}"
    return "Birthday not found."

# Retrieves upcoming birthdays for the next 7 days
@input_error
def birthdays(book: AddressBook) -> str:
    upcoming_birthdays = book.get_upcoming_birthdays()
    if upcoming_birthdays:
        return '\n'.join([f"{user['name']} - {user['congratulation_date']}" for user in upcoming_birthdays])
    return "No birthdays in the next 7 days."

# Parses user input to separate command and arguments
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

# Main loop to run the bot and handle user commands
@input_error
def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        if user_input == "":
            continue
        else: command, args = parse_input(user_input)
        match command:
            case "close" | "exit":
                print("Goodbye!")
                sys.exit(0)
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, book))
            case "change":
                print(change_contact(args, book))
            case "phone":
                print(get_phone(args, book))
            case "all":
                print(get_all_contacts(book))
            case "add-birthday":
                print(add_birthday(args, book))
            case "show-birthday":
                print(show_birthday(args, book))
            case "birthdays":
                print(birthdays(book))
            case "help":
                print('Available commands: \n'
                      '\t"add" username number \n'
                      '\t"all" \n'
                      '\t"change" username old_number new_number \n'
                      '\t"close" \n'
                      '\t"exit" \n'
                      '\t"help" \n'
                      '\t"hello" \n'
                      '\t"phone": username \n'
                      '\t"add-birthday": username birthday(DD.MM.YYYY) \n'
                      '\t"show-birthday": username \n'
                      '\t"birthdays" \n'
                       )
            case _:
                print("I don't know this command.\n"
                      "Use 'help' to get the list of all commands."
                      )

if __name__ == "__main__":
    main()
