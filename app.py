from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from back_end.add_drone import add_drone
from back_end.take_over import take_over
from back_end.add_restaurant import add_restaurant
from back_end.add_ingredient import addIngredient
from back_end.add_employee import add_employee
from back_end.add_owner import add_owner
from back_end.add_worker_role import add_worker_role
from back_end.add_pilot_role import add_pilot_role
from back_end.add_service import addService
from back_end.display_views import displayOwner, displayPilot, displayLocation, displayEmployee, displayIngredient, displayService
from back_end.add_location import add_location
from back_end.join_swarm import join_swarm
from back_end.start_funding import start_funding
from back_end.leave_swarm import leave_swarm
from back_end.load_drone import load_drone
from back_end.refuel_drone import refuel_drone
from back_end.fly_drone import fly_drone
from back_end.purchase_ingredient import purchase_ingredient
from back_end.remove_drone import remove_drone
from back_end.remove_ingredient import remove_ingredient
from back_end.remove_pilot_role import remove_pilot_role
from back_end.fire_employee import fire_employee
from back_end.hire_employee import hire_employee
from back_end.manage_service import manage_service

app = Flask(__name__)
 
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mrokey123@'
app.config['MYSQL_DB'] = 'restaurant_supply_express'
 
mysql = MySQL(app)
 
 
@app.route('/', methods=['GET', 'POST'])
def main(): 
    return render_template('main_page.html')

#======= ROUTE FOR STORE PROCEDURE=======

# ROUTE FOR ADD OWNER
@app.route('/add-owner/', methods=['GET', 'POST'])
def be_add_owner():
    return add_owner()

# ROUTE FOR ADD DRONE
@app.route('/add-drone/', methods=['GET', 'POST'])
def backend_add_drone():
    return add_drone()
# ROUTE FOR TAKE OVER
@app.route('/take-over/', methods=['GET', 'POST'])
def backend_take_over():
    return take_over()

# ROUTE FOR ADD RESTAURANT  
@app.route('/add-restaurant/', methods=['GET', 'POST'])
def backend_add_restaurant():
    return add_restaurant()

# ROUTE FOR ADD INGREDIENT 
@app.route('/add-ingredient/', methods=['GET', 'POST'])
def be_add_ingredient():
    return addIngredient()


# ROUTE FOR ADD EMPLOYEE
@app.route('/add-employee/', methods=['GET', 'POST'])
def be_add_employee():
    return add_employee()

# ROUTE FOR ADD WORKER ROLE
@app.route('/add-worker-role/', methods=['GET', 'POST'])
def be_add_worker_role():
    return add_worker_role()
    
# ROUTE FOR ADD PILOT ROLE
@app.route('/add-pilot-role/', methods=['GET', 'POST'])
def be_add_pilot_role():
    return add_pilot_role()


# ROUTE FOR ADD SERVICE
@app.route('/add-service/', methods=['GET', 'POST'])
def be_add_service():
    return addService()


# ROUTE FOR ADD LOCATION
@app.route('/add-location/', methods=['GET', 'POST'])
def be_add_location():
    return add_location()

#ROUTE FOR JOIN SWARM
@app.route('/join-swarm/', methods=['GET', 'POST'])
def be_join_swarm():
    return join_swarm()

#ROUTE FOR START FUNDING
@app.route('/start-funding/', methods=['GET', 'POST'])
def be_start_funding():
    return start_funding()

#ROUTE FORE LEAVE SWARM
@app.route('/leave-swarm/', methods=['GET', 'POST'])
def be_leave_swarm():
    return leave_swarm()


#ROUTE FORE LOAD DRONE
@app.route('/load-drone/', methods=['GET', 'POST'])
def be_load_drone():
    return load_drone()

#ROUTE FORE REFUEL DRONE
@app.route('/refuel-drone/', methods=['GET', 'POST'])
def be_refuel_drone():
    return refuel_drone()

#ROUTE FORE FLY DRONE
@app.route('/fly-drone/', methods=['GET', 'POST'])
def be_fly_drone():
    return fly_drone()

#ROUTE FORE PURCHASE INGREDIENT
@app.route('/purchase-ingredient/', methods=['GET', 'POST'])
def be_purchase_ingredient():
    return purchase_ingredient()

#ROUTE FORE REMOVE DRONE
@app.route('/remove-drone/', methods=['GET', 'POST'])
def be_remove_drone():
    return remove_drone()

#ROUTE FOR REMOVE INGREDIENT
@app.route('/remove-ingredient/', methods=['GET', 'POST'])
def be_remove_ingredient():
    return remove_ingredient()


#ROUTE FOR REMOVE PILOT ROLE
@app.route('/remove-pilot-role/', methods=['GET', 'POST'])
def be_remove_pilot_role():
    return remove_pilot_role()

#ROUTE FOR HIRE EMPLOYEE
@app.route('/hire-employee/', methods=['GET', 'POST'])
def be_hire_employee():
    return hire_employee()

#ROUTE FOR FIRE EMPLOYEE
@app.route('/fire-employee/', methods=['GET', 'POST'])
def be_fire_employee():
    return fire_employee()

#ROUTE FOR MANAGE SERVICE
@app.route('/manage-service/', methods=['GET', 'POST'])
def be_manage_service():
    return manage_service()



#====== ROUTE FOR DISPLAYING==========

# ROUTE FOR DISPLAY INGREDIENT MANAGEMENT 
@app.route('/ingredient-management/', methods=['GET', 'POST'])
def be_ingredient_management():
    return render_template('ingredient_main_page.html')

# ROUTE FOR DISPLAY RESTAURANT MANAGEMENT 
@app.route('/restaurant-management/', methods=['GET', 'POST'])
def be_restaurant():
    return render_template('restaurant_main_page.html')

# ROUTE FOR DISPLAY USER MANAGEMENT 
@app.route('/user-management/', methods=['GET'])
def be_user_management():
    return render_template('user_main_page.html')

# ROUTE FOR DISPLAY SERVICE MANAGEMENT 
@app.route('/service-management/', methods=['GET'])
def be_service_management():
    return render_template('service_main_page.html')

# ROUTE FOR DISPLAY DRONE MANAGEMENT
@app.route('/drone-management/', methods=['GET', 'POST'])
def backend_drone_management():
    return render_template('drone_main_page.html')


# ROUTE FOR DISPLAY OWNER
@app.route('/view-owner/', methods=['GET'])
def be_displayOwner():
    return displayOwner()


# ROUTE FOR DISPLAY EMPLOYEE
@app.route('/view-employee/', methods=['GET'])
def be_displayEmployee():
    return displayEmployee()

# ROUTE FOR DISPLAY PILOT
@app.route('/view-pilot/', methods=['GET'])
def be_displayPilot(): 
    return displayPilot()


# ROUTE FOR DISPLAY LOCATION
@app.route('/view-location/', methods=['GET'])
def be_displayLocation(): 
    return displayLocation()

# ROUTE FOR DISPLAY INGREDIENT
@app.route('/view-ingredient/', methods=['GET'])
def be_displayIngredient(): 
    return displayIngredient()


# ROUTE FOR DISPLAY SERVICE
@app.route('/view-service/', methods=['GET'])
def be_displayService(): 
    return displayService()




if __name__ == '__main__':
    app.debug = True
    app.run()