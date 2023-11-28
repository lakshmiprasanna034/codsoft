class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        self.contacts[contact.name] = contact
        print(f"Contact added successfully: {contact.name}")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("\nContact List:")
            for name, contact in self.contacts.items():
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, query):
        results = []
        for name, contact in self.contacts.items():
            if query.lower() in contact.name.lower() or query in contact.phone_number:
                results.append((name, contact))
        return results

    def update_contact(self, name, field, new_value):
        if name in self.contacts:
            setattr(self.contacts[name], field, new_value)
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

def get_contact_details():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    return Contact(name, phone_number, email, address)

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            contact = get_contact_details()
            contact_manager.add_contact(contact)

        elif choice == '2':
            contact_manager.view_contacts()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            results = contact_manager.search_contact(query)
            if results:
                print("\nSearch Results:")
                for name, contact in results:
                    print(f"Name: {contact.name}, Phone: {contact.phone_number}")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            name = input("Enter name of the contact to update: ")
            field = input("Enter field to update (name/phone_number/email/address): ")
            new_value = input(f"Enter new {field}: ")
            contact_manager.update_contact(name, field, new_value)

        elif choice == '5':
            name = input("Enter name of the contact to delete: ")
            contact_manager.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
