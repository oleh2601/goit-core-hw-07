from datetime import datetime, date, timedelta
from phone import Field

class Birthday(Field):
    """Class to represent a birthday with validation and formatting capabilities."""

    def __init__(self, value: str):
        super().__init__(value)
        try:
            Birthday.validate_bday(Birthday.string_to_date(value))
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        
    @staticmethod
    def validate_bday(birth_date: date):
        """Validates that the birth date is not in the future."""
        if birth_date > date.today():
            raise ValueError("Date cannot be in the future") 
        
    @staticmethod
    def string_to_date(date_string: str):
        """Converts a string date to a datetime.date object."""
        return datetime.strptime(date_string, "%d.%m.%Y").date()

    @staticmethod
    def date_to_string(date: date):
        """Converts a datetime.date object to a string in DD.MM.YYYY format."""
        return date.strftime("%d.%m.%Y")
