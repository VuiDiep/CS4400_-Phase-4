from flask import Flask, render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)
 
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mrokey123@'
app.config['MYSQL_DB'] = 'restaurant_supply_express'
 
mysql = MySQL(app)


def take_over():
    if request.method == "POST":
        details = request.form
        userName = details['ip_username']
        id = details['ip_id']
        tag = details['ip_tag']

        cur = mysql.connection.cursor()

        if userName == '' or len(userName) > 40:
            return 'Invalid Username Input!'
        
        if id == '' or len(id) > 40:
            return 'Invalid ID Input!'
        try: 
            tag = int(tag)
        except: 
            return 'Invalid Tag Input!'


        query2 = "SELECT manager FROM delivery_services"
        cur.execute(query2)
        for item2 in cur:
            if (userName == item2[0]):
                return ("USERNAME is a MANAGER!!")

        cur.execute('SELECT username FROM pilots')
        flag3 = False
        for item3 in cur:
            if item3[0] == userName:
                flag3 = True
                break
        if (flag3 == False):
            return 'The employee is not a valid pilot!'


        cur.execute('SELECT id FROM delivery_services')
        flag = False
        for item in cur: 
            if (item[0] == id):
                flag = True
                break
        if (flag == False):
            return 'ID Does Not Exist!'

        cur.execute("SELECT tag FROM drones WHERE tag = '%s' and id = '%s' "%(tag, id))
        flag = cur.fetchall()
        if len(flag) != 1:
            return 'Tag does not exist!'

        cur.execute("SELECT id FROM work_for WHERE username = '%s' "%(userName))
        flag4 = False
        for item4 in cur:
            if item4[0] == id:
                flag4 = True
                break
        if flag4 == False:
            return 'This employee or this drone is not currently working for this service!'

        

        cur.execute('SELECT swarm_id, swarm_tag FROM drones')
        flag2 = False
        for item1 in cur:
            if item1[0] == id and item1[1] == tag:
                flag2 = True
                break
        if (flag2 == False):
            return 'Drone is not a leader!'

    

        cur.callproc('takeover_drone', [userName, id, tag])
        mysql.connection.commit()
        cur.close()
        return 'Successfully Updated!'
    return render_template('take_over.html')




