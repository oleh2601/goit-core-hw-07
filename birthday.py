from datetime import datetime, date, timedelta

class Birthday():   

    def __init__(self, date_str: str):
        try:
            self.date = Birthday.string_to_date(date_str)
            Birthday.validate_bday(self.date)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        
    @staticmethod
    def validate_bday(birth_date: date):
        if birth_date > date.today() > 0:
            raise ValueError("Date cannot be in the future") 
        
    @staticmethod
    def string_to_date(date_string):
        return datetime.strptime(date_string, "%d.%m.%Y").date()

    @staticmethod
    def date_to_string(date):
        return date.strftime("%d.%m.%Y")


    