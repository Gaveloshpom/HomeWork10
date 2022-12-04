from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass


class Phones(Field):
    pass


class AddressBook(UserDict):
    def add_record(self, name):
        self.data[name] = Record(name)

    def change_contact_name(self, old_name, new_name: str):
        old = old_name.name.value
        self.data[new_name], self.data[old_name.name.value].name.value = self.data[old_name.name.value], new_name
        del self.data[old]
        return f"Name {old} changed to {new_name}."

    def get_records(self):
        print(self.data)
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
    def __init__(self, name, phone=None):
        self.name = Name(name)
        self.phones = [Phones(phone)] if phone else []



    def get_info(self):
        phone_info = ''

        for phone in self.phones:
            phone_info += f'{phone.value}, '

        return f'{self.name.value} : {phone_info[:-2]}'

    def add_phone(self, phone):
        self.phones.append(Phones(phone))
        return f"{phone} added to {self.name.value}"

    def delete_phone(self, number):
        for values in self.phones:
            if values.value == number:
                self.phones.remove(values)
                return f"Pnone number {number} deleted for user {self.name.value}."
        else:
            return f"Can`t find {number} for user {self.name.value}"

    def change_phone(self, phones):
        for phone in phones:
            if not self.delete_phone(phone):
                self.add_phone(phone)














