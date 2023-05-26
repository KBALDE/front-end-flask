# Flask

Microweb framework of python 

Third party lib can be added

```sh
pip install vrtualenv
brew install virtualenv
# create
## be in a given directory
virtualenv myEnv -p python3
# activate
source myEnv/bin/activate

# now install
pip install flask

# check 
pip freeze
# can check if flask is well installed 
# using ipython

```

Now let's create an app

```python
from flask import Flask

app=Flask(__name__)
```
Flask uses WSGI, Web Service Gateway Interface

Now when calling the app, we need to route the call to a function view.

The use of decorators

````python
@app.route('/')
def index():
    return "Hello Word"
````


### Env variables
We can run our application using the env varaible

```sh
export FLASK_APP=app-1.py
```

And then by runnig the app

```sh
flask run  
```
# other way to run
programmatically
````py
if __name__='__main__':
    app.run(host='0.0.0.0', port=3000)

````

And then
```sh
python app-1.py  

# dynamic routing
```python
@app.route('/<name>')
# define the view
def print_name(name):
    return " Hi, {}".format(name)

```
# command tool
```sh
flask --help
```

# Request and response cycle
when falsk receieve a call, it willc reate an object and make it available for the view function

Falsk uses context
- application context 
- request context

need to view funxtion to call

# REST

# SQLite
sqlite3 with python

```python
import sqlite3
conn= sqlite3.connect("books.sqlite")
# run  python script to creat the database
python db.py
```

Now we need to have a cursor object => used to execute SQL statements




