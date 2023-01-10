from flask import Flask, render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)
 
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mrokey123@'
app.config['MYSQL_DB'] = 'restaurant_supply_express'
 
mysql = MySQL(app)


def remove_drone():
    if request.method == "POST":
        details = request.form
        id = details['ip_id']
        tag = details['ip_tag']

        cur = mysql.connection.cursor()

        if id == '' or len(id) > 40:
            return 'Invalid ID Input!'
        try: 
            tag = int(tag)
        except: 
            return 'Invalid Tag Input!'


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

        
        cur.execute('SELECT id, tag FROM payload')
        for item1 in cur:
            if item1[0] == id and item1[1] == tag:
                return 'Drone Is Carrying Ingredient!'

        cur.execute('SELECT swarm_id, swarm_tag FROM drones')
        flag2 = False
        for item1 in cur:
            if item1[0] == id and item1[1] == tag:
                flag2 = True
                break
        if (flag2 == True):
            return 'Drone is currently leading swarms!'
            







    
        cur.callproc('remove_drone', [id, tag])
        mysql.connection.commit()
        cur.close()
        return 'Successfully Deleted!'
    return render_template('remove_drone.html')