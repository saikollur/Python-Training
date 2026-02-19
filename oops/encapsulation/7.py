class LibraryBook:
    def __init__(self, title):
        self.title = title
        self.__available = True

    def issue_book(self):
        if self.__available:
            self.__available = False
            print(f'"{self.title}" has been issued.')
        else:
            print(f'"{self.title}" is already issued.')

    def return_book(self):
        if not self.__available:
            self.__available = True
            print(f'"{self.title}" has been returned.')
        else:
            print(f'"{self.title}" was not issued.')

    def display_status(self):
        if self.__available:
            print(f'"{self.title}" is available in the library.')
        else:
            print(f'"{self.title}" is currently issued.')


book = LibraryBook("Atomic Habits")

book.display_status()
book.issue_book()
book.issue_book()
book.display_status()
book.return_book()
book.return_book()
book.display_status()
