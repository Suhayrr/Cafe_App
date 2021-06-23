# Suheers pop app cafe mini project

Command line application built in Python for a pop up cafe to create orders for customers. Data is stored in a MYSQL database and allows users to perform CRUD operations on their data. 

As a user I want to:
Create a product, order or courier and add it to a list.
Read products,orders and couriers in a list and display it onto the terminal.
Update a product, order or courier.
Delete a product, order or courier.

Data is also cached to a csv file as backup.

## Getting Started.

Under the repo name click clone or download
Click on use HTTPs, copy the clone URL of the repo
In the terminal go on the working directory where you want to clone the project
Use the git clone command and paste the clone URL then press enter :

$ git clone https://github.com/your-username/your-repositary.git
On your local machine go inside of the pop-up-cafe directory :
$ cd Miniproject

## Create a Docker Container for MySQL database

1. Ensure you have Docker Desktop installed and running (you can check with docker -v).
2. Run the following command inside the directory in a terminal. This will create both the client and server for us which is running on localhost.
$ docker-compose up -d
​ You should get the following output:

Creating mysql_container   ... done
Creating adminer_container ... done

3. Navigate to the following URL to ensure that you can see the Adminer interface:
http://localhost:8080/

4. Fill in the username (root) and password field (password), leave the database field blank.

5. Select SQL Command on the left.

6. We'll create our own database with:

CREATE DATABASE cafe;

7. We'll create our tables with the following commands using the sql command:
 
create table Products (prod_id INT NOT NULL AUTO_INCREMENT, prod_name VARCHAR(255), prod_price FLOAT, PRIMARY KEY (prod_id));

create table Couriers (c_id INT NOT NULL AUTO_INCREMENT, c_name VARCHAR(255), c_number BIGINT, PRIMARY KEY (c_id));

create table Orders (order_id INT NOT NULL AUTO_INCREMENT, order_name VARCHAR(255), order_add VARCHAR(255), order_phone INT, order_courier VARCHAR(255), order_status VARCHAR(255), order_items VARCHAR(255), PRIMARY KEY (order_id));

## Creating And Activating The Virtual Environment
Creating the virtual environment

On macOS and Linux:

python3 -m venv .venv
On Windows:

py -m venv .venv
Activate the virtual environment Windows:

$ source venv/Scripts/activate
MacOS/Unix:

$ source venv/bin/activate

To install the requirements text file, run the following command in the terminal:

$ pip install -r requirements.txt

## Running the tests
Check that the codes are passing the test. From the tests directory, run:

$ pytest tests.py -v

## Author
Suheer Hassan



