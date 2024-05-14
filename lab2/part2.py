filename = "address_book.txt"
contacts = {}

def load_contacts(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file.readlines():
                contacts[line.split(",")[0]] = line.split(",")[1]

    except FileNotFoundError:
        print("File not found.")

def add_contact(file_name, name, email):
    try:
        with open(file_name, 'a') as file:
            file.write("\n")
            file.write(name + "," + email)
        contacts[name] = email
        print("Contact added successfully!")
    except:
        print("Error opening file")

load_contacts(filename)

while(1):
    print("1. Add a new contact\n2. Search for a contact\n3. List all contacts\n4. Exit")

    try:
        option = int(input("Your option: "))

        if option == 4:
            print("Good Bye!")
            break
        elif option == 1:
            name = input("Enter the name: ")
            email = input("Enter the email: ")
            add_contact(filename, name, email)
        elif option == 2:
            name = input("Enter name you want to search: ")
            if name in contacts.keys():
                print(name, "email is:", contacts[name])
            else:
                print("Contact not found")
        elif option == 3:
            for name, email in contacts.items():
                print("Name:", name, ", Email:", email)
        else:
            print("Wrong option try again")
        print()

    except:
        print("Wrong option try again")