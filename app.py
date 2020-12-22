from flask import Flask, request, render_template
import pyodbc

conn = pyodbc.connect('Driver={SQL SERVER};' 
		'server=LAPTOP-9KIO0AR0;' 
		'database=ADVENTUREWORKS2019;' 
		'trusted_connection=YES;')
app = Flask(__name__,static_url_path='/static')

#index.html
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


#infodisp.html
@app.route('/infodisp')
def infodisp():
    query = "SELECT * FROM HumanResources.EmployeePayHistory" 
    with conn.cursor() as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
    return render_template('infodisp.html', data=data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        name = request.form['name']
        mail = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        query = "INSERT INTO contact VALUES('" + name + "', '" + mail + "', '" + phone + "', '" + message + "');"
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO contact VALUES(?, ?, ?, ?)", (name, mail, phone, message))

    return render_template('contact.html')

if __name__ == '__main__':
	app.run(debug=True)