class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.available = True

class Loan:
    def __init__(self, book_id, user, due_date):
        self.book_id = book_id
        self.user = user
        self.due_date = due_date
        self.returned = False