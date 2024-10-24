from phone import Phone
from phone import Name


class Record:
    
    def __init__(self, name: Name, phones=None):
        self.name = Name(name)
        self.phones = phones if phones else []

    def add_phone(self, phone_number: str):
        phone = Phone(phone_number)
        self.phones.append(phone)
        
    
    def remove_phone(self, phone_number: str):
        phone = Phone(phone_number)
        for p in self.phones:
            if p.value == phone.value:
                self.phones.remove(p)
                return
        print(f"{phone_number} not found")
    
    def edit_phone(self, old_number, new_number):
            old_phone = Phone(old_number)
            new_phone = Phone(new_number)
            if not new_phone.validate_phone():
                raise ValueError(f"The number {new_number} isn't valid")
            for index, phone in enumerate(self.phones):
                if phone.value == old_phone.value:
                    self.phones[index] = new_phone
                    return
            raise ValueError(f"The number {old_number} wasn't found in contacts")

    def find_phone(self, phone_number: str) -> Phone:
        phone = Phone(phone_number)
        for element in self.phones:
            if element.value == phone.value:
                return element
        return None


    