# debug mode: export FLASK_ENV=development
# run via: export FLASK_APP=app.py, flask run
# run via: export FLASK_APP=app.py, python -m flask run
# run via: python app.py, note: must have app.run() in app.py
# web server will run at http://127.0.0.1:5000/

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

# if __name__ == '__main__':
#    app.run()
#    app.run(debug = True)
