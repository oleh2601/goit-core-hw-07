from collections import UserDict
from record import Record

class AddressBook(UserDict):

    def clear_all_records(self):
        self.data = {}

    def add_record(self, record: Record):
        self.data[record.name.value] = record
    
    def delete_record(self, name: str):
        del self.data[name]
    
    def find(self, name: str) -> Record:
        return self.data.get(name, None)
    
    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())
    
