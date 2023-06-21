from flask import Flask, render_template
import os

#Import the file database.py
import database as db

#1. ACCESS TO A FILE TO SEND A LOCALHOST
#Create a variable where is the name of directory's application
#We're going to use it a function's os (dirname) to access a absolute path
#file: directory which we want to go into

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

#2. JOIN SRC AND TEMPLATES WITH FILE PROJECT
template_dir = os.path.join(template_dir,'src', 'templates')

#3. INITIALIZING FLASK TO EXECUTE THE APLICATION IN LOCALHOST
#Declarate a variable to initializing with Flask
#Template folder is the directory we are (index.html) is the same as template_dir
#App will look for the template to execute into an scren
app = Flask(__name__, template_folder = template_dir )

#4. TO SET UP THE PRINCIPAL ROUTE

#Application routes

@app.route("/")
def home():
    return render_template('index.html')
# We want to show the template index.html so we need to import render template from flask
 
@app.route("/books")
def books():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM books")

    mybooks = cursor.fetchall()
    books_array =[]
    books_col_Names = [column[0] for column in cursor.description]
    for book in mybooks:
        books_array.append(dict(zip(books_col_Names, book)))
    cursor.close()
    return render_template('table_books.html' , data = books_array )


# TO EXECUTE THE APPLICATION
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)    
#with app.run we're going to indicate that the app is going to be in development





