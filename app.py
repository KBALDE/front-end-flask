from flask import Flask, jsonify, request

import sqlite3

app=Flask(__name__)


@app.route('/')
def index():
    return "Hello Word"

@app.route('/<name>')
# define the view
def print_name(name):
    return " Hi, {}".format(name)

# books list
books_list=[
    {
        'id':1,
        "authors":"Chinua Achebe",
        "country":"Nigeria",
        "language":"English",
    },
    {
        'id':2,
        "authors":"Hans Christian Andersen",
        "country":"Denmark",
        "language":"Danish",
    },
    {
        'id':3,
        "authors":"Dante Alighieri",
        "country":"Italy",
        "language":"Italian",
    }
]

def db_connection():
    conn=None
    try:
        conn=sqlite3.connect("books.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn

@app.route('/books', methods=['GET', 'POST'])
def books():
    conn=db_connection()
    cursor=conn.cursor()
    if request.method == 'GET':
        cursor=conn.execute("SELECT * FROM books")
        books=[
            dict(id=row[0], authors=row[1], country=row[2], language=row[3])
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)
        else:
            'Nothing found', 404

    if request.method == 'POST':
        new_author = request.json['authors']
        new_country = request.json['country']
        new_language = request.json['language']
        sql_command = """INSERT INTO books (authors, country, language)
        VALUES (?,?,?)"""
        cursor.execute(sql_command, [new_author, new_country, new_language])
        conn.commit()
        return f"Book with the id : {cursor.lastrowid} created successfully"
      

@app.route('/book/<int:id>', methods=['GET', 'PUT', 'DELETE']) 
def single_book(id):
    conn=db_connection()
    cursor=conn.cursor()
    book=None
    if request.method=='GET':
        cursor.execute("SELECT * FROM books WHERE id=?", (id,))
        rows= cursor.fetchall()
        for r in rows:
            book=r
        if book is not None:
            return jsonify(book), 200
        else:
            return "Something wrong", 404
        
    if request.method=='PUT':
        sql="""UPDATE books
        SET author=?,
        country=?,
        language=?
        WHERE id=?"""
        author=request.json['authors']
        country=request.json['country']
        language=request.json['language']
        updated_book={
            "id":id,
            "authors":author,
            "country":country,
            "language":language
        }
        conn.execute(sql, [author, country, language, id])
        conn.commit()
        return jsonify(updated_book), 200
    
    if request.method=='DELETE':
        sql="""DELETE FROM books WHERE id=?"""
        conn.execute(sql, [id])
        conn.commit()
        return "The book with id: {} has been deleted.".format(id), 200
   
            

if __name__ == '__main__':
    app.run(debug=True)