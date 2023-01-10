from flask import Flask, render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)
 
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mrokey123@'
app.config['MYSQL_DB'] = 'restaurant_supply_express'
 
mysql = MySQL(app)


def load_drone():
    if request.method == "POST":
        details = request.form
        id = details['ip_id']
        tag = details['ip_tag']
        barcode = details['ip_barcode']
        more_packages = details['ip_more_packages']
        price = details['ip_price']


        cur = mysql.connection.cursor()

        if id == '' or len(id) > 40:
            return 'Invalid ID Input!'
        try: 
            tag = int(tag)
        except: 
            return 'Invalid Tag Input!'
        if barcode == '' or len(barcode) > 40:
            return 'Invalid Barcode Input!'
        try: 
            more_packages = int(more_packages)
        except: 
            return 'Invalid More Packages Input!'
        try: 
            price = int(price)
        except: 
            return 'Invalid Price Input!'

        if more_packages <= 0:
            return 'Package has to be greater than 0!'

        cur.execute("SELECT id FROM delivery_services WHERE id = '%s'" % id); 
        res = cur.fetchall()
        if (len(res) != 1):
            return ('Input ID Does Not Exist!')


        cur.execute("SELECT id, tag FROM drones WHERE id = '%s' and tag = '%s'" % (id, tag))
        res = cur.fetchall()
        if (len(res) != 1):
            return ('Input Drone Does Not Exist!')


        cur.execute("SELECT barcode FROM ingredients WHERE barcode = '%s'" % barcode)
        res = cur.fetchall()
        if (len(res) != 1):
            return ('Input Barcode Does Not Exist!')


        cur.execute("SELECT hover FROM drones WHERE id = '%s' and tag = '%s'" %(id, tag))
        droneLoc = cur.fetchall()
        cur.execute("SELECT home_base FROM delivery_services WHERE id = '%s'" %(id))
        homeLoc = cur.fetchall()
        if droneLoc != homeLoc:
            return 'Drone is not at the service homebase!'

        cur.execute("SELECT capacity FROM drones WHERE id = '%s' and tag = '%s'" %(id, tag))
        droneCap = cur.fetchone()[0]
        cur.execute("SELECT sum(quantity) from payload group by id having id = '%s'" %(id))
        quan = cur.fetchone()[0]
        if int(droneCap - quan) < more_packages:
            return 'Capicity Overload!!'



        cur.callproc('load_drone', [id, tag, barcode, more_packages, price])
        mysql.connection.commit()
        cur.close()
        return 'Successfully Updated!'
    return render_template('load_drone.html')