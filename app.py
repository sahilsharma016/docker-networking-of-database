from flask import Flask, request, jsonify, render_template
import pymysql

app = Flask(__name__)

# Database connection
connection = pymysql.connect(
    # host='localhost',

    # for docker use 
    # host="host.docker.internal",

    # for docker mysql
    # host="172.17.0.2",

    # for network 
    # this didn't work 
    host='mysqldbcontainer',

    user='root',
    
    # password="Password@123"
    password='root',
    database='database1',
    port=3306
)

def create_table():
    with connection.cursor() as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            email VARCHAR(100) NOT NULL,
            password VARCHAR(100) NOT NULL
        )
        """)
    connection.commit()


@app.route('/', methods=['GET', 'POST'])
def home():
    return "Add /register in searchbox"


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        with connection.cursor() as cursor:
            cursor.execute("""
            INSERT INTO users (username, email, password)
            VALUES (%s, %s, %s)
            """, (username, email, password))
        connection.commit()
        
        return jsonify({"message": "User registered successfully!"})
    
    return render_template('register.html')


@app.route('/users', methods=['GET'])
def get_users():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
    
    user_list = []
    for user in users:
        user_data = {
            'id': user[0],
            'username': user[1],
            'email': user[2]
        }
        user_list.append(user_data)
    
    return jsonify(user_list)

if __name__ == '__main__':
    create_table()
    app.run(debug=True, host='0.0.0.0')

# docker run -d --env MYSQL_ROOT_PASSWORD="root" --env MYSQL_DATABASE="user" --name mySQLDB mysql
# docker run -p 5000:5000 flask_db_py