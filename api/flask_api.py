# save this as app.py
'''
from flask import Flask, request
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
'''
import psycopg2
from flask import Flask,request,jsonify
app = Flask(__name__)
db_params = {
    "dbname": "learning",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432"
}

# Establish the connection
try:
    connection = psycopg2.connect(**db_params)
    print("Connected to the database")

    # Create a cursor object
    cursor = connection.cursor()


except Exception as e:
    print(f"Error connecting to the database: {e}")


def my_data_insert(data):
    name=data["name"]
    age=data["age"]
    cursor.execute("""
        INSERT INTO public.student(name, age) VALUES (%s, %s)""", (name, age))
    print(data)
    connection.commit()
    return "Function processed the input"
@app.route("/attempt",methods=["POST"])
def attempt():
    print("attempt succesful")
    my_obj= request.get_json()
    my_value=my_data_insert(my_obj)
    return my_value


def data_select():
    try:
        # Execute the SQL command
        cursor.execute("SELECT * FROM student;")

        # Fetch all the rows
        db_data = cursor.fetchall()

        return db_data
    except Exception as e:
        print(f"Error selecting data: {e}")
        return None


@app.route("/get_data",methods=["GET"])
def get_data():
    print("data has been succesfully sent")
    recieved_data = data_select()
    print(recieved_data)
    if recieved_data is None:
        return jsonify({"error": "Unable to retrieve data"}), 500
    print(recieved_data)
    return jsonify(recieved_data), 200


if __name__=='__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)

