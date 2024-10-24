class Field:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass
    


class Phone(Field):

    def __init__(self, value: str):
        self.value = value
        if not self.validate_phone():
            raise ValueError("Invalid phone number")
        

    def validate_phone(self) -> bool:
        if self.value.isnumeric() and (len(self.value) == 10):
                return True
        return False

    def __str__(self):
        return str(self.value)   