from collections import UserDict


class Field:
    def __int__(self, value):
        self.value = value

class Name(Field):
    pass


class Phones(Field):
    pass


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def get_records(self):
        return self.data

    def record_checker(self, name):
        return bool(self.data.get(name))

    def get_by_name(self, name):
        return self.data.get(name)

    def remove_record(self, name):
        del self.data[name]

    def search(self, value):
        if self.record_checker(value):
            return self.get_by_name(value)

        for record in self.get_records().values():
            for phone in record.phones:
                if phone.value == value:
                    return record

        raise ValueError("Contact with this value does not exist.")




class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def get_info(self):
        phone_info = ''

        for phone in self.phones:
            phone_info += f'{phone.value}, '

        return f'{self.name.value} : {phone_info[:-2]}'

    def add_phone(self, phone):
        self.phones.append(Phones(phone))

    def delete_phone(self, phone):
        for record_phone in self.phones:
            if record_phone.value == phone:
                self.phones.remove(record_phone)
                return True
        return False

    def change_phone(self, phones):
        for phone in phones:
            if not self.delete_phone(phone):
                self.add_phone(phone)










