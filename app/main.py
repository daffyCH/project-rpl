from flask import Flask, request, jsonify, render_template
from app.service import LibraryService
from app.notification import send_reminder

app = Flask(__name__)
library = LibraryService()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/books", methods=["POST"])
def add_book():
    data = request.json
    book = library.add_book(data["title"], data["author"])
    return jsonify(book.__dict__)

@app.route("/books/search")
def search():
    q = request.args.get("q", "")
    return jsonify(library.search_books(q))

@app.route("/borrow", methods=["POST"])
def borrow():
    data = request.json
    result = library.borrow_book(data["book_id"], data["user"])
    return jsonify(result)

@app.route("/return", methods=["POST"])
def return_book():
    data = request.json
    result = library.return_book(data["book_id"])
    return jsonify(result)

@app.route("/loans")
def loans():
    return jsonify(library.get_loans())

@app.route("/reminder/<user>/<int:book_id>")
def reminder(user, book_id):
    send_reminder(user, book_id)
    return {"status": "sent"}

if __name__ == "__main__":
    app.run(debug=True)