class Field:
    """Base class for fields like Name and Phone, which contain a value."""
    
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    """Class representing a contact's name."""
    pass

class Phone(Field):
    """Class representing a contact's phone number with validation."""

    def __init__(self, value: str):
        self.value = value
        if not self.validate_phone():
            raise ValueError(f"Invalid phone number: {value}. Must be exactly 10 digits.")
        
    def validate_phone(self) -> bool:
        """Validates that the phone number is numeric and contains exactly 10 digits."""
        return self.value.isnumeric() and len(self.value) == 10

    def __str__(self):
        return str(self.value)
