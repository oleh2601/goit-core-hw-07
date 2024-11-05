from collections import UserDict
from datetime import date, timedelta
from birthday import Birthday
from record import Record

class AddressBook(UserDict):
    """Class to represent an address book, inheriting from UserDict to store records."""

    def delete(self):
        """Clears all records from the address book."""
        self.data = {}    

    def add_record(self, record: Record):
        """Adds a new record to the address book."""
        self.data[record.name.value] = record
    
    def delete_record(self, name: str):
        """Deletes a record from the address book by name."""
        del self.data[name]
    
    def find(self, name: str) -> Record:
        """Finds a record by name."""
        return self.data.get(name, None)
    
    def __str__(self):
        """Returns a string representation of all records in the address book."""
        return '\n'.join(str(record) for record in self.data.values())
    
    @staticmethod
    def prepare_user_list(user_data):
        """Prepares a list of users with birthdays."""
        prepared_list = []
        for user in user_data:
            prepared_list.append({"name": user["name"], "birthday": Birthday.string_to_date(user["birthday"])})
        return prepared_list
    
    @staticmethod
    def adjust_for_weekend(birthday: date):
        """Adjusts the birthday to the next working day if it falls on a weekend."""
        if birthday.weekday() >= 5:  # If Saturday or Sunday
            return AddressBook.find_next_weekday(birthday, 0)  # Move to next Monday
        return birthday

    def get_upcoming_birthdays(self, days=7):
        """Finds users whose birthdays fall within the next 7 days."""
        upcoming_birthdays = []
        today = date.today()

        for record in self.data.values():
            if record.birthday:
                birthday_this_year = Birthday.string_to_date(record.birthday.value).replace(year=today.year)
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                
                if 0 <= (birthday_this_year - today).days <= days:
                    birthday_this_year = AddressBook.adjust_for_weekend(birthday_this_year)
                    congratulation_date_str = Birthday.date_to_string(birthday_this_year)
                    upcoming_birthdays.append({"name": record.name.value, "congratulation_date": congratulation_date_str})
                
        return upcoming_birthdays
    
    @staticmethod
    def find_next_weekday(start_date: date, weekday: int):
        """Finds the next occurrence of a given weekday."""
        days_ahead = weekday - start_date.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return start_date + timedelta(days=days_ahead)
