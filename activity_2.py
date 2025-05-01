class Library:
    def __init__(self, list_of_books, name):
        self.booklist = list_of_books
        self.name = name
        self.lenDict = {}
    def displayBooks(self):
        print("We have the following books in our library: ", {self.name})
        for book in self.booklist:
            print(book)

    def lendBook(self, user, book):
        if book not in self.bookslist:
            print("Sorry, we do not have that book.")
        elif book in self.lenDict:
            print("The book is already being used by", self.lenDict[book])
        else:
            self.lenDict[book] = user
            print("Lender-book database has been updated. You can take the book now")
    def addbook(self, book):
        self.booklist.append(book)
        print(f"{book}has been added to the book list.")
    def returnBook(self, book):
        if book in self.lenDict:
            del self.lenDict[book]
            print("Book has been returned.")
        else:
            print("That book wasnt borrowed by us.")

if __name__ == '__main__':
    books = Library(['Python', 'Rich dad poor dad', 'Harry potter', 'C++ basics', 'Algorithms by CLRS', 'Lets upskill', 'english'])
user_name = input('Welcome to our library! Please enter your name: ')

while True:
    print(f"\nhello {user_name}, welcome to the {books.name} library, please choose an option.")
    print("1. Display books\n2. Lend a book\n3. Add a book\n4. Return a book\n5. quit")

    user_choice = input("Enter your choice to continue: ")

    if user_choice not in ['1', '2', '3', '4', '5']:
        print("Please enter a valid option")
        continue


    if user_choice == '1':
        books.displayBooks()
    elif user_choice == '2':
        book = input("Enter the name of the book you want to lend: ")
        books.lendBook(user_name, book)
    elif user_choice == '3':
        book = input("Enter the name of the book you want to add: ")
        books.addBook(book)
    elif user_choice == '4':
        book = input("Enter the name of the book you want to return : ")    
        books.returnBook(book)
    elif user_choice == '5':
        print("Thank you for using the library",{user_name}, "Goodbye!")
        break

