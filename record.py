from phone import Phone
from phone import Name
from birthday import Birthday

class Record:
    """Class to represent a contact record which contains a name, a list of phone numbers, and an optional birthday."""

    def __init__(self, name: Name, phones: list[Phone] = None):
        self.name = Name(name)
        self.phones = phones if phones else []
        self.birthday = None

    def add_birthday(self, birth_date: str):
        """Adds a birthday to the contact."""
        self.birthday = Birthday(birth_date)

    def add_phone(self, phone_number: str):
        """Adds a phone number to the contact."""
        phone = Phone(phone_number)
        self.phones.append(phone)

    def __str__(self):
        """Returns a string representation of the contact with name and phones."""
        phones_str = ', '.join(str(phone) for phone in self.phones)
        return f"{self.name} {phones_str} {self.birthday}"
    
    def remove_phone(self, phone_number: str):
        """Removes a specific phone number from the contact."""
        phone = Phone(phone_number)
        for p in self.phones:
            if p.value == phone.value:
                self.phones.remove(p)
                return
        print(f"{phone_number} not found")
    
    def edit_phone(self, old_number, new_number):
        """Edits an existing phone number for the contact."""
        new_phone = Phone(new_number)
        for index, phone in enumerate(self.phones):
            if phone.value == old_number:
                self.phones[index] = new_phone
                return
        raise ValueError(f"The number {old_number} wasn't found in contacts")

    def find_phone(self, phone_number: str) -> Phone:
        """Finds and returns a specific phone number if it exists."""
        phone = Phone(phone_number)
        for element in self.phones:
            if element.value == phone.value:
                return element
        return None
