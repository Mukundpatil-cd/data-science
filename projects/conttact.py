class contact:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
    
    def __str__(self):
        return f"{self.name}-{self.phone}"
    
contacts=[]

def add_con():
    name=input("enter name")
    phone=int(input("enter the number "))
    contacts=contact(name,phone)
    contacts.append(contact)
    print("contact added")
    
def show():
    for c in contacts:
        print(c)
def save_contacts():
    with open("contacts.txt", "w") as file:
        for c in contacts:
            file.write(f"{c.name},{c.phone}\n")
    print("Contacts saved to file!")

def load_contacts():
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts.append(contact(name, phone))
        print("Contacts loaded from file!")
    except FileNotFoundError:
        print("No saved contacts found.")

    # Main menu for testing
    if __name__ == "__main__":
        while True:
            print("\nContact Manager")
            print("1. Add Contact")
            print("2. Show Contacts")
            print("3. Save Contacts")
            print("4. Load Contacts")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                add_con()
            elif choice == "2":
                show()
            elif choice == "3":
                save_contacts()
            elif choice == "4":
                load_contacts()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
