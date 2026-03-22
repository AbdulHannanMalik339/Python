class libary:
    def __init__(self, list ,name):
        self.booklist = list
        self.name = name
        self.lenddict = {}

    def displaybook(self):
        print(f"We have following books in our library : {self.name}")
        for book in self.booklist:
            print(book)

    def lendbook(self, user, book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book: user})
            print("Lender-Book database has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lenddict[book]}")

    def addbook(self, book):
        self.booklist.append(book)
        print("Book has been added to the book list")

    def returnbook(self, book):
        self.lenddict.pop(book)

if __name__ == '__main__':

    booklist = ['Python', 'Rich Dad Poor Dad', 'Harry Potter', 'C++', 'Java']
    library = libary(booklist, 'Central')

    while True:
        print(f"Welcome to the {library.name} library")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.displaybook()

        elif choice == "2":
            book = input("Enter the name of the book you want to lend: ")
            user = input("Enter your name: ")
            library.lendbook(user, book)

        elif choice == "3":
            book = input("Enter the name of the book you want to add: ")
            library.addbook(book)

        elif choice == "4":
            book = input("Enter the name of the book you want to return: ")
            library.returnbook(book)

        else:
            print("Not a valid option")

    print("Press q to quit and c to continue")
    user_choice2 = ""
    while(user_choice2 != "c" and user_choice2 != "q"):
        user_choice2 = input()
        if user_choice2 == "q":
            exit()

        elif user_choice2 == "c":
            continue
        