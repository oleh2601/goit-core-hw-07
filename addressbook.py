from collections import UserDict
from datetime import date, timedelta
from birthday import Birthday
from record import Record

class AddressBook(UserDict):

    def delete(self):
        self.data = {}    

    def add_record(self, record: Record):
        self.data[record.name.value] = record
    
    def delete_record(self, name: str):
        del self.data[name]
    
    def find(self, name: str) -> Record:
        return self.data.get(name, None)
    
    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())
    
    def prepare_user_list(user_data):
        prepared_list = []
        for user in user_data:
            prepared_list.append({"name": user["name"], "birthday": Birthday.string_to_date(user["birthday"])})
        return prepared_list
    

    def adjust_for_weekend(birthday: date):
        if birthday.weekday() >= 5:
            return AddressBook.find_next_weekday(birthday, 0)
        return birthday


    def get_upcoming_birthdays(book: list[dict], days=7):

        users = book
        upcoming_birthdays = []
        today = date.today()

        for user in users:
            birthday_this_year = user["birthday"].replace(year=today.year)
            if birthday_this_year < today:
                birthday_this_year = user["birthday"].replace(year=today.year + 1)
                
            if 0 <= (birthday_this_year - today).days <= days:
                birthday_this_year = AddressBook.adjust_for_weekend(birthday_this_year)
                congratulation_date_str = Birthday.date_to_string(birthday_this_year)
                upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})
                
        return upcoming_birthdays
    
    def find_next_weekday(start_date: date, weekday):
        days_ahead = weekday - start_date.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return start_date + timedelta(days=days_ahead)

