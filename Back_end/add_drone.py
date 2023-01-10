from flask import Flask, render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)
 
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mrokey123@'
app.config['MYSQL_DB'] = 'restaurant_supply_express'
 
mysql = MySQL(app)


def add_drone():
    if request.method == "POST":
        details = request.form
        id = details['ip_id']
        tag = details['ip_tag']
        fuel = details['ip_fuel']
        capacity = details['ip_capacity']
        sales = details['ip_sales']
        flown_by = details['ip_flown_by']
        cur = mysql.connection.cursor()

        if id == '' or len(id) > 40:
            return 'Invalid ID Input!'
        try: 
            tag = int(tag)
        except: 
            return 'Invalid Tag Input!'
        try: 
            fuel = int(fuel)
        except: 
            return 'Invalid Fuel Input!'
        try: 
            capacity = int(capacity)
        except: 
            return 'Invalid Capacity Input!'
        try: 
            sales = int(sales)
        except: 
            return 'Invalid Sales Input!'
        if flown_by == '' or len(flown_by) > 40:
            return 'Invalid Flown By Input!'



        query1 = "SELECT id, tag FROM drones"
        cur.execute(query1)
        for item1 in cur:
            if id == item1[0] and int(tag) == item1[1]:
                return 'Drone Already Exist!'

        cur.execute('SELECT id FROM delivery_services')
        flag = False
        for item in cur: 
            if (item[0] == id):
                flag = True
                break
        if (flag == False):
            return 'ID Does Not Exist!'
                
        query3 = "SELECT username FROM pilots"
        cur.execute(query3)
        flag = False
        for item3 in cur:
            if (flown_by == item3[0]):
                flag = True
                break
        if (flag == False):
                return 'Pilot does not exist!'

        cur.execute("select id from work_for where username = '%s'" %(flown_by))
        flag5 = cur.fetchone()[0]
        if flag5 != id:
            return 'Pilot is not the same id with drones'




        cur.callproc('add_drone', [id, tag, fuel, capacity, sales, flown_by])
        mysql.connection.commit()
        cur.close()
        return 'successfully added a new drone'
    return render_template('add_drone.html')



