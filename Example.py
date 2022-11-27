from collections import UserDict


class Field:
    field = ''


class Name(Field):
    field = ""


class Phones(Field):
    field = []


class AddressBook(UserDict):


    def get_name(self, value):
        return self.data[value]


    # def get_name_by_phones(self, phone):
    #     return self.data[phone]


class Record(Name, Phones):

    def add(self, dict: UserDict, name, *args):
        # a = AddressBook()
        dict[name] = args
        print(dict)

    def clear(self, dict: UserDict, name):
        dict.data.pop(name)
        print(dict)

    def change(self, dict: UserDict, name, *args):
        dict[name] = args
        print(dict)


# a = AddressBook()
# b = Record()
# b.add(a, "hello", 700, 800, 900)
# b.change(a, "hello", 760)






