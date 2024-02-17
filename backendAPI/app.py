""""This code is a simple Flask application that provides post register 
job applications and retrieve customer data from a MySQL database."""

from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql

# Initialize Flask App
app = Flask(__name__)
CORS(app)

# Database Connection Function:
def db_connection():
    conn=None
    try:                      #Inside the function, it attempts to connect to the MySQL database using pymysql.
        conn = pymysql.connect(
        host='localhost',
        database='myproject',
        user='root',
        password='1131',
        cursorclass=pymysql.cursors.DictCursor
        )
    except pymysql.Error as e:
        print(e)
    return conn

# POST method
reglist=[]
@app.route('/register', methods=['POST'])   #Defines an endpoint '/register' that accepts POST requests.
def register():
    conn = db_connection()
    cursor = conn.cursor()
    reglist.clear()
    cursor.execute("SELECT * FROM regdata") 
    for row in cursor.fetchall():
        reglist.append(row)

    if request.method == 'POST':
        try:
            new_ename = request.form['ename']
            new_dob = request.form['date_of_birth']
            new_email = request.form['email']
            new_number = request.form['mobnumber']
            new_education = request.form['education']
            new_job = request.form['job']
            new_experience = request.form["experience"]
            new_rurl = request.form["resumeurl"]
            new_app_no= len(reglist) + 1
        except KeyError as e:
            return jsonify({'error': f'KeyError: {e}'}), 400 
        
        query = "INSERT INTO regdata (app_no,ename, date_of_birth, email, mobnumber, education, job, experience, resumeurl) VALUES ({},'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(new_app_no,new_ename, new_dob, new_email, new_number, new_education, new_job, new_experience, new_rurl)
        cursor.execute(query)
        conn.commit()
        return jsonify({'message': 'registered successfully'}), 200


# GET method  
@app.route('/getCustomers/<int:app_no>', methods=['GET']) #Defines an endpoint '/getCustomers/int:app_no' that accepts GET requests with an integer parameter 'app_no'.
def getCustomers(app_no):
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        reglist.clear()
        cursor.execute("SELECT * FROM regdata Where app_no={}".format(app_no)) 
        for row in cursor.fetchall():
            reglist.append(row)
        
        if len(reglist) > 0:
            return jsonify(reglist), 200
        else:
            return jsonify("Nothing Found"), 404

   

if __name__ == '__main__': #Checks if the script is executed directly.
    app.run(debug=True)