import sys
from functools import wraps
from addressbook import AddressBook 
from record import Record
from phone import Phone
from birthday import Birthday

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except IndexError:
            return "Please provide valid data."
        except TypeError:
            return "Please provide valid data."
        except KeyError:
            return "Please provide valid data."
    return inner

@input_error
def add_contact(args, book: AddressBook) -> str:
    if len(args) < 2:
        return "Please provide both a name and a phone number."
    if len(args) > 2:
        return "Too many arguments. Only provide a name and a phone number."
    name, phone = args
    record = book.find(name)
    message = "Contact updated."
    if not record:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def get_all_contacts(book: AddressBook) -> str:
    if book.data:
        return str(book)    
    else:
        return "No contacts found."

@input_error
def get_phone(args, book: AddressBook) -> str:
    name = args[0]
    record = book.find(name)
    if record:
        return ', '.join(str(phone) for phone in record.phones)
    return "Contact not found."

@input_error
def change_contact(args, book: AddressBook) -> str:
    if len(args) < 3:
        return "Please provide the correct number of arguments: name, old phone, and new phone."
    if len(args) > 3:
        return "Too many arguments. Only provide a name, an old number and a new number."
    name, old_phone, new_phone = args
    record = book.find(name)
    if record:
        try:
            record.edit_phone(old_phone, new_phone)
            return "Contact updated."
        except ValueError as e:
            return str(e)
    return "Contact not found."

@input_error
def add_birthday(args, book: AddressBook) -> str:
    if len(args) < 2:
        return "Please provide both a name and a birthday date in a format 'DD.MM.YYYY'."
    if len(args) > 2:
        return "Too many arguments. Only provide a name and a birthday date in a format 'DD.MM.YYYY'."
    name, birthday_str = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.add_birthday(birthday_str)
    return "Birthday added."

@input_error
def show_birthday(args, book: AddressBook) -> str:
    if len(args) < 1:
        return "Please provide a name of an existing contact"
    if len(args) > 1:
        return "Too many arguments. Please only provide a name of an existing contact."
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    if record and record.birthday:
        return f"{name}'s birthday is on {record.birthday.date_to_string(record.birthday.date)}"
    return "Birthday not found."

@input_error
def birthdays(book: AddressBook) -> str:
    upcoming_birthdays = book.get_upcoming_birthdays()
    if upcoming_birthdays:
        return '\n'.join([f"{user['name']} - {user['congratulation_date']}" for user in upcoming_birthdays])
    return "No birthdays in the next 7 days."

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
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
                      '  "add" username number \n'
                      '  "all" \n'
                      '  "change" username old_number new_number \n'
                      '  "close" \n'
                      '  "exit" \n'
                      '  "help" \n'
                      '  "hello" \n'
                      '  "phone" username \n'
                      '  "add-birthday" username birthday \n'
                      '  "show-birthday" username \n'
                      '  "birthdays" \n'
                       )
            case _:
                print("I don't know this command.\n"
                      "Use 'help' to get the list of all commands."
                      )

if __name__ == "__main__":
    main()
