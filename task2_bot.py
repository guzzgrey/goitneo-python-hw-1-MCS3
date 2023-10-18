def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command format. Use 'add username phone'."
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command format. Use 'change username phone'."
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact changed."


def get_contact(args, contacts):
    if len(args) != 1:
        return "Invalid command format. Use 'phone username'."
    name = args[0]
    if name not in contacts:
        return "Contact not found."
    return contacts[name]


def get_all(contacts):
    if not contacts:
        return "No contacts found."
    contact_list = "\n".join(
        [f"{name} : {phone}" for name, phone in contacts.items()])
    return contact_list


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    print("Commands:")
    print(" - 'hello' - to start the conversation")
    print(" - 'add -> (username phone)' - to add a contact")
    print(" - 'change -> (username phone)' - to change a contact's phone number")
    print(" - 'phone -> (username)' - to get a contact's phone number")
    print(" - 'all' - to get all contacts")
    print(" - 'close' or 'exit' - to exit the bot")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_contact(args, contacts))
        elif command == "all":
            print(get_all(contacts))
        else:
            print("Invalid command format or unknown command.")


if __name__ == "__main__":
    main()
