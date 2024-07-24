# save this as app.py
from flask import Flask,request

app = Flask(__name__)
def db_insert(student_record):
    print(student_record)
    return "recieved"
@app.route("/")
def hello():
    return "Hello, World!"
@app.route("/greetings",methods=["POST"])
def hi():
    myobjr= request.get_json()
    my_value = db_insert(myobjr)
    return my_value
app.run(host='0.0.0.0', port=5000,debug=True)

