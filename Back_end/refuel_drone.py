from flask import Flask, render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)
 
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mrokey123@'
app.config['MYSQL_DB'] = 'restaurant_supply_express'
 
mysql = MySQL(app)


def refuel_drone():
    if request.method == "POST":
        details = request.form
        id = details['ip_id']
        tag = details['ip_tag']
        more_fuel = details['ip_more_fuel']

        cur = mysql.connection.cursor()


        if id == '' or len(id) > 40:
            return 'Invalid ID Input!'
        try: 
            tag = int(tag)
        except: 
            return 'Invalid Tag Input!'
        try: 
            more_fuel = int(more_fuel)
        except: 
            return 'Invalid More Fuel Input!'

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

        cur.execute("SELECT hover FROM drones WHERE tag = '%s' and id = '%s' "%(tag, id))
        droneLoc = cur.fetchall()
        cur.execute("SELECT home_base FROM delivery_services WHERE id = '%s' "%(id))
        swarmLoc = cur.fetchall()
        if droneLoc != swarmLoc:
            return 'This Drone Is Not At Homebase!'


        cur.callproc('refuel_drone', [id, tag, more_fuel])
        mysql.connection.commit()
        cur.close()
        return 'Successfully Updated!'
    return render_template('refuel_drone.html')