from datetime import datetime, timedelta
from app.models import Book, Loan

class LibraryService:
    def __init__(self):
        self.books = []
        self.loans = []
        self.counter = 1

    def add_book(self, title, author):
        book = Book(self.counter, title, author)
        self.books.append(book)
        self.counter += 1
        return book

    def search_books(self, keyword):
        return [
            b.__dict__ for b in self.books
            if keyword.lower() in b.title.lower()
        ]

    def borrow_book(self, book_id, user):
        for b in self.books:
            if b.id == book_id and b.available:
                b.available = False
                due_date = datetime.now() + timedelta(days=7)
                loan = Loan(book_id, user, due_date)
                self.loans.append(loan)
                return {"message": "borrowed", "due_date": str(due_date)}
        return {"error": "not available"}

    def return_book(self, book_id):
        for loan in self.loans:
            if loan.book_id == book_id and not loan.returned:
                loan.returned = True

                late_days = (datetime.now() - loan.due_date).days
                fine = max(0, late_days * 1000)

                for b in self.books:
                    if b.id == book_id:
                        b.available = True

                return {"fine": fine}
        return {"error": "loan not found"}

    def get_loans(self):
        return [
            {
                "book_id": l.book_id,
                "user": l.user,
                "due_date": str(l.due_date),
                "returned": l.returned
            }
            for l in self.loans
        ]