
-- RUNNING THE APP:
	If you don't already have them, install Python 3.7, pip, mySQL Server and mySQL Workbench.

-- PROJECT STRUCTURE: This repository contains 3 main things:
	SQL files for setting up the database
	Python with Flask
	HTML (frontend) files
-- Prerequisites to run the webserver:
	Make sure you have all of the dependencies (see Installing the dependencies, below)

-- INSTALLING THE DEPENDENCIES:
	Make sure you have googleChrome or Safari on your computer, if not download it from your web browser.
	Make sure you have Python3.7 64 bits, if you don't have it,  go to https://www.python.org/ and install python3
	Make sure you have installed Mysql Workbench, Mysql server, and Mysql connectors. If you dont have it, go to https://dev.mysql.com/downloads/installer/, 	and install everything as recommended. Make sure to remember the 	password for your server. You must then go to backend file and go line 8 in every 	file*.py and change the password to your SQL server's password.
	Open a shell (Terminal or Command Prompt), enter the directory and run pip install to the needed python modules not already installed on python.
	If after running any code, if any library is missing, type in the command prompt under the directory in which python is installed "pip install" plus the 	name of the library

-- WHAT'S WHERE:
	back_end file is where we save all the Python with Flask files
	Templates file is where we save all the HTML files
	cs4400_database_v2 schema_and_data.sql contains the  sql code to create our database schema and populate it with values.
	cs4400_procedure_shell_v2 disjoint_employees_owners.sql contains the store procedure SQL and view 
	
-- HOW TO RUN THIS APP:
	open app.py file then run "Flask run" at terminal, it should pop up  "Running on http://127.0.0.1:5000". 
	Go to your browser and insert http://127.0.0.1:5000
-- ACCOMPLISHED:
	we have created 2 folders for backend and frontend. For the backend, we use Python with Flask to connect to MySQL server. The files for this folder 	are used to handle the logic of the web page. For the frontend, we use HTML to take user input and interact with the backend to display database and 	conduct all the related methods.
-- DISTRIBUTED:
	all 3 of us handle both frontend and backend. Each of us handle about 10 store procedures and views
