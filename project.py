from validator_collection import validators
import pyfiglet
import csv
import os
class Contact:
    def __init__(self, name, number, mail):
        self.name = name
        self.number = number
        self.mail = mail
    def __init__(self):
        ...
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        words = name.split()
        for word in words:
            if not word.isalpha():
                 print("Invalid name, Please try again")
                 self.name = input("Enter name:")
            else:
                self._name = name

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if not number.isdigit():
            print("Invalid phone number, Please try again")
            self.number = input("Enter phone number:")
        else:
             self._number = number

    @property
    def mail(self):
        return self._mail

    @mail.setter
    def mail(self, mail):
        try :
            if validators.email(mail):
                self._mail = mail
        except Exception as e:
            print("Invalid mail, Please try again")
            self.mail = input("Enter mail:")

    def validate_name(name):
        words = name.split()
        for word in words:
            if not word.isalpha():
                 raise ValueError
            else:
                return name

    def validate_number(number):
        if not number.isdigit():
            raise ValueError
        else:
             return number

    def validate_mail(mail):
        try :
            if validators.email(mail):
                return mail
        except:
            raise ValueError

def add_contact():
    contact = Contact()
    contact.name = input("Enter contact name: ")
    contact.number = input("Enter phone number: ")
    contact.mail = input("Enter email: ")
    text = pyfiglet.figlet_format("Contact added successfully.",font="rectangles",)
    print(text)
    try:
        with open("contacts.csv", "r") as f:
            reader = csv.reader(f)
            if len(list(reader)) == 0:
                with open("contacts.csv", "w", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow(["Name", "Phone", "Email"])
    except:
        with open("contacts.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Phone", "Email"])
    with open("contacts.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([contact.name, contact.number, contact.mail])

def search_contact():
    if os.path.getsize("contacts.csv") == 0:
        print("No contacts available to search within")
    else:
        found = False
        key = input("Enter the name: ")
        with open("contacts.csv", "r") as f:
            rows = csv.reader(f)
            for row in rows:
                name,phone,mail = row
                names = name.split()
                for i in names:
                    if key.lower() == i.lower():
                        print()
                        print("Contact found:")
                        print("Name:", name)
                        print("Phone:", phone)
                        print("Mail:", mail)
                        print()
                        found = True
            if not found:
                print("Contact not found:")

def delete_index(delete_list, rows):
            del_index = input("Enter which Contact you want to delete (just the number of it in this list): ")
            if del_index.isdigit():
                if(int(del_index)-1 < len(delete_list)):
                    print (rows)
                    with open("contacts.csv", "w") as f:
                        writer = csv.writer(f)
                        for row in rows:
                            if delete_list[int(del_index)-1] == row:
                                continue
                            writer.writerow(row)
                else:
                    print("index out of range.")
                    delete_index(delete_list,rows)

            else:
                print("Wrong value")
                delete_index(delete_list,rows)


def delete_contact():
    if os.path.getsize("contacts.csv") == 0:
        print("No contacts available to be deleted.")
    else:
        delete_list = []
        rows2 = []
        key = input("Enter contact name to delete: ")
        with open("contacts.csv", "r") as f:
            rows = csv.reader(f)
            for row in rows:
                rows2.append(row)
                name= row[0]
                names = name.split()
                for i in names:
                    if key.lower() == i.lower():
                        delete_list.append(row)
            if len(delete_list) == 1:
                print("1 contact found having this name")
                if len(delete_list[0][0]) == 1:
                    name = delete_list[0]
                    print("Name:", delete_list[0])
                    print("Phone:", delete_list[1])
                    print("Mail:", delete_list[2])
                else:
                    name = delete_list[0][0]
                    print("Name:", delete_list[0][0])
                    print("Phone:", delete_list[0][1])
                    print("Mail:", delete_list[0][2])
                with open("contacts.csv", "w") as f:
                    writer = csv.writer(f)
                    for row in rows:
                        if name == row[0]:
                            continue
                        writer.writerow(row)
            elif len(delete_list) > 1:
                print(len(delete_list), "contacts found having this name")
                i = 0
                while i < len(delete_list):
                    print(i + 1)
                    print("Name:", delete_list[i][0])
                    print("Phone:", delete_list[i][1])
                    print("Mail:", delete_list[i][2])
                    print()
                    i = i + 1
                delete_index(delete_list,rows2)
            else :
                print("No contacts found with that name.")


def display_contacts():
    if os.path.getsize("contacts.csv") == 0:
        print("No contacts available to be displayed.")
    else:
        with open("contacts.csv", "r") as f:
            rows = csv.reader(f)
            for row in rows:
                name,phone,mail = row
                if name == "Name":
                    continue
                print()
                print("Name:", name)
                print("Phone:", phone)
                print("Mail:", mail)
                print()

while True:
    text = pyfiglet.figlet_format("phonebook.", font="larry3d", width = 100, justify="right")
    print(text)
    print("1.Add contact\t2.Search contact\t3.Delete contact\t4.Display contacts\t5.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        display_contacts()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")