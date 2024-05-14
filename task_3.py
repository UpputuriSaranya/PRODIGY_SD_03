import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}
    return contacts

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def add_contact(contacts):
    name = input("Enter the name of the contact: ")
    phone = input("Enter the phone number of the contact: ")
    email = input("Enter the email address of the contact: ")
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"{name} has been added to your contacts.")

def view_contacts(contacts):
    if not contacts:
        print("Your contact list is empty.")
    else:
        print("Your contacts:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def edit_contact(contacts):
    name = input("Enter the name of the contact you want to edit: ")
    if name in contacts:
        print("Current details:")
        print(f"Name: {name}, Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
        contacts[name]["phone"] = input("Enter the new phone number (leave blank to keep current): ") or contacts[name]["phone"]
        contacts[name]["email"] = input("Enter the new email address (leave blank to keep current): ") or contacts[name]["email"]
        save_contacts(contacts)
        print(f"{name}'s contact details have been updated.")
    else:
        print(f"{name} is not in your contacts.")

def delete_contact(contacts):
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"{name} has been deleted from your contacts.")
    else:
        print(f"{name} is not in your contacts.")

def main():
    contacts = load_contacts()
    while True:
        print("\nMENU:")
        print("1. Add a new contact")
        print("2. View contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
