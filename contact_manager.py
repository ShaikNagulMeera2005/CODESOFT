# contact_manager.py

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    print(f"Contact {name} added.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact(contacts):
    search = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if search.lower() in contact['name'].lower() or search in contact['phone']:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    matching_contacts = [contact for contact in contacts if name.lower() in contact['name'].lower()]

    if len(matching_contacts) == 0:
        print("Contact not found.")
    elif len(matching_contacts) == 1:
        contact = matching_contacts[0]
        print(f"Found: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
        new_name = input("Enter new name (leave blank to keep current): ")
        new_phone = input("Enter new phone number (leave blank to keep current): ")
        new_email = input("Enter new email (leave blank to keep current): ")
        new_address = input("Enter new address (leave blank to keep current): ")
        if new_name:
            contact['name'] = new_name
        if new_phone:
            contact['phone'] = new_phone
        if new_email:
            contact['email'] = new_email
        if new_address:
            contact['address'] = new_address
        print(f"Contact {name} updated.")
    else:
        print(f"Found {len(matching_contacts)} contacts with the name {name}:")
        for i, contact in enumerate(matching_contacts, 1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
        
        phone = input("Enter the phone number of the contact to update: ")
        contact_to_update = next((contact for contact in matching_contacts if contact['phone'] == phone), None)
        
        if contact_to_update:
            print(f"Found: {contact_to_update['name']}, Phone: {contact_to_update['phone']}, Email: {contact_to_update['email']}, Address: {contact_to_update['address']}")
            new_name = input("Enter new name (leave blank to keep current): ")
            new_phone = input("Enter new phone number (leave blank to keep current): ")
            new_email = input("Enter new email (leave blank to keep current): ")
            new_address = input("Enter new address (leave blank to keep current): ")
            if new_name:
                contact_to_update['name'] = new_name
            if new_phone:
                contact_to_update['phone'] = new_phone
            if new_email:
                contact_to_update['email'] = new_email
            if new_address:
                contact_to_update['address'] = new_address
            print(f"Contact {name} with phone number {phone} updated.")
        else:
            print("Contact with the specified phone number not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    matching_contacts = [contact for contact in contacts if name.lower() in contact['name'].lower()]

    if len(matching_contacts) == 0:
        print("Contact not found.")
    elif len(matching_contacts) == 1:
        contact = matching_contacts[0]
        contacts.remove(contact)
        print(f"Contact {contact['name']} with phone number {contact['phone']} deleted.")
    else:
        print(f"Found {len(matching_contacts)} contacts with the name {name}:")
        for i, contact in enumerate(matching_contacts, 1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
        
        phone = input("Enter the phone number of the contact to delete: ")
        contact_to_delete = next((contact for contact in matching_contacts if contact['phone'] == phone), None)
        
        if contact_to_delete:
            contacts.remove(contact_to_delete)
            print(f"Contact {contact_to_delete['name']} with phone number {contact_to_delete['phone']} deleted.")
        else:
            print("Contact with the specified phone number not found.")

def main():
    contacts = []
    print("Contact Manager")
    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
