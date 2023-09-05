from flask import Flask, render_template, request, redirect, url_for

from flask_mysqldb import MySQL
app= Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="1234"
app.config['MYSQL_DB']="carbon_collect"

mysql=MySQL(app)



@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/carbon-credit')
def carbon_credit():
        return render_template('carbon-credit.html')

@app.route('/carbon-sequestration')
def carbon_sequestration():
        return render_template('carbon-sequestration.html')

@app.route('/commercial')
def commercial():
        return render_template('commercial.html')

@app.route('/future')
def future():
        return render_template('future.html')


@app.route('/isro-carbon-project')
def isro_carbon_project():
        return render_template('isro-carbon-project.html')

@app.route('/references')
def references():
        return render_template('references.html')



@app.route('/comments', methods=["POST", "GET"])
def comments():
    if request.method=="POST":
        fname=request.form["fname"]
        lname=request.form["lname"]
        village=request.form["village"]
        zip=request.form["zip"]
        phone=request.form["phone"]
        comments=request.form["comments"]

 
        
        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO users(first_name,last_name,village,zip_code,mobile_no, comments) VALUES (%s,%s,%s,%s,%s,%s)",(fname,lname,village,zip,phone,comments))

        mysql.connection.commit()

        cur.close()

        return "you have successfuly registered!!"
    else:
        return render_template('comments.html')

@app.route('/welcome')
def welcome():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    data =cur.fetchall()
    
    cur.close()
    
    return render_template('welcome.html', users=data)

    

if __name__=="__main__":
    app.run(debug=True)


