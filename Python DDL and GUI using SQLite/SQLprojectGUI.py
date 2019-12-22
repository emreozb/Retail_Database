from tkinter import *
from PIL import ImageTk, Image 
import sqlite3
import json

root = Tk()
root.title('Retail Store Database')
root.geometry('{}x{}'.format(1300, 600))

# Create a database or connect to one
conn = sqlite3.connect('retail_database.sqlite')

# Create cursor
c = conn.cursor()


# Create Submit Function For Database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('retail_database.sqlite')
    # Create cursor
    c = conn.cursor()
    # Insert Into Table
    c.execute("INSERT INTO customer(cust_id, c_name, c_phone, c_address, c_email) VALUES (?,?,?,?,?)",[(box_cust_id.get()),(box_c_name.get()),(box_c_phone.get()),(box_c_address.get()),(box_c_email.get())])
    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close
    # Clear Text Boxes
    box_cust_id.delete(0, END)
    box_c_name.delete(0, END)
    box_c_phone.delete(0, END)
    box_c_address.delete(0, END)
    box_c_email.delete(0, END)

def submit1():
    # Create a database or connect to one
    conn = sqlite3.connect('retail_database.sqlite')
    # Create cursor
    c = conn.cursor()
    # Insert Into Table
    c.execute("INSERT INTO employee(e_id, e_ssn, e_name, e_title, e_start_date, e_end_date) VALUES (?,?,?,?,?,?)",[(box_e_id.get()),(box_e_ssn.get()),(box_e_name.get()),(box_e_title.get()),(box_e_start_date.get()),(box_e_end_date.get())])
    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close
    # Clear Text Boxes
    box_cust_id.delete(0, END)
    box_c_name.delete(0, END)
    box_c_phone.delete(0, END)
    box_c_address.delete(0, END)
    box_c_email.delete(0, END)

def submit2():
    # Create a database or connect to one
    conn = sqlite3.connect('retail_database.sqlite')
    # Create cursor
    c = conn.cursor()
    # Insert Into Table
    c.execute("INSERT INTO invoice(invoice_id, cust_id, store_id, total_amount) VALUES (?,?,?,?)",[(box_invoice_id.get()),(box_cust_id.get()),(box_store_id.get()),(box_total_amount.get())])
    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close
    # Clear Text Boxes
    box_invoice_id.delete(0, END)
    box_cust_id.delete(0, END)
    box_store_id.delete(0, END)
    box_total_amount.delete(0, END)

def submit3():
    # Create a database or connect to one
    conn = sqlite3.connect('retail_database.sqlite')
    # Create cursor
    c = conn.cursor()
    # Insert Into Table
    c.execute("INSERT INTO stock(stk_id, stk_address, stk_item, stk_type) VALUES (?,?,?,?)",[(box_stk_id.get()),(box_stk_address.get()),(box_stk_item.get()),(box_stk_type.get())])
    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close
    # Clear Text Boxes
    box_stk_id.delete(0, END)
    box_stk_address.delete(0, END)
    box_stk_item.delete(0, END)
    box_stk_type.delete(0, END)

def submit4():
    # Create a database or connect to one
    conn = sqlite3.connect('retail_database.sqlite')
    # Create cursor
    c = conn.cursor()
    # Insert Into Table
    c.execute("INSERT INTO supplier(supplier_id, supplier_name, supplier_address) VALUES (?,?,?)",[(box_supplier_id.get()),(box_supplier_name.get()),(box_supplier_address.get())])
    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close
    # Clear Text Boxes
    box_supplier_id.delete(0, END)
    box_supplier_name.delete(0, END)
    box_supplier_address.delete(0, END)

def submit5():
    # Create a database or connect to one
    conn = sqlite3.connect('retail_database.sqlite')
    # Create cursor
    c = conn.cursor()
    # Insert Into Table
    c.execute("INSERT INTO product(product_id, price, total_stock) VALUES (?,?,?)",[(box_product_id.get()),(box_price.get()),(box_total_stock.get())])
    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close
    # Clear Text Boxes
    box_product_id.delete(0, END)
    box_price.delete(0, END)
    box_total_stock.delete(0, END)

def submit6():
    # Create a database or connect to one
    conn = sqlite3.connect('retail_database.sqlite')
    # Create cursor
    c = conn.cursor()
    # Insert Into Table
    c.execute("INSERT INTO store(store_id, s_phone, s_address) VALUES (?,?,?)",[(box_store_id.get()),(box_s_phone.get()),(box_s_address.get())])
    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close
    # Clear Text Boxes
    box_store_id.delete(0, END)
    box_s_phone.delete(0, END)
    box_s_address.delete(0, END)


def submit7():
    # Create a database or connect to one
    conn = sqlite3.connect('retail_database.sqlite')
    # Create cursor
    c = conn.cursor()
    # Insert Into Table
    c.execute("INSERT INTO online_cust(cust_id, username, password) VALUES (?,?,?)",[(box_cust_id.get()),(box_username.get()),(box_password.get())])
    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close
    # Clear Text Boxes
    box_cust_id.delete(0, END)
    box_username.delete(0, END)
    box_password.delete(0, END)

def submit8():
    # Create a database or connect to one
    conn = sqlite3.connect('retail_database.sqlite')
    # Create cursor
    c = conn.cursor()
    # Insert Into Table
    c.execute("INSERT INTO supplies(supplier_id, product_id) VALUES (?,?)",[(box_supplier_id.get()),(box_product_id.get())])
    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close
    # Clear Text Boxes
    box_supplier_id.delete(0, END)
    box_product_id.delete(0, END)

def submit9():
    # Create a database or connect to one
    conn = sqlite3.connect('retail_database.sqlite')
    # Create cursor
    c = conn.cursor()
    # Insert Into Table
    c.execute("INSERT INTO purchases(product_id, username, password, cust_id) VALUES (?,?,?,?)",[(box_product_id.get()),(box_username.get()),(box_password.get()),(box_cust_id.get())])
    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close
    # Clear Text Boxes
    box_product_id.delete(0, END)
    box_username.delete(0, END)
    box_password.delete(0, END)
    box_cust_id.delete(0, END)

def submit10():
    # Create a database or connect to one
    conn = sqlite3.connect('retail_database.sqlite')
    # Create cursor
    c = conn.cursor()
    # Insert Into Table
    c.execute("INSERT INTO works(store_id, e_id, manager_id) VALUES (?,?,?)",[(box_store_id.get()),(box_e_id.get()),(box_manager_id.get())])
    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close
    # Clear Text Boxes
    box_store_id.delete(0, END)
    box_e_id.delete(0, END)
    box_manager_id.delete(0, END)

def submit11():
    # Create a database or connect to one
    conn = sqlite3.connect('retail_database.sqlite')
    # Create cursor
    c = conn.cursor()
    # Insert Into Table
    c.execute("INSERT INTO online_acc(username, password) VALUES (?,?)",[(box_username.get()),(box_password.get())])
    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close
    # Clear Text Boxes
    box_username.delete(0, END)
    box_password.delete(0, END)

def submit12():
    # Create a database or connect to one
    conn = sqlite3.connect('retail_database.sqlite')
    # Create cursor
    c = conn.cursor()
    # Insert Into Table
    c.execute("INSERT INTO contains(store_id, product_id) VALUES (?,?)",[(box_store_id.get()),(box_product_id.get())])
    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close
    # Clear Text Boxes
    box_store_id.delete(0, END)
    box_product_id.delete(0, END)

def submit13():
    # Create a database or connect to one
    conn = sqlite3.connect('retail_database.sqlite')
    # Create cursor
    c = conn.cursor()
    # Insert Into Table
    c.execute("INSERT INTO cust_invoice(cust_id, invoice_id) VALUES (?,?)",[(box_cust_id.get()),(box_invoice_id.get())])
    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close
    # Clear Text Boxes
    box_cust_id.delete(0, END)
    box_invoice_id.delete(0, END)

def submit14():
    # Create a database or connect to one
    conn = sqlite3.connect('retail_database.sqlite')
    # Create cursor
    c = conn.cursor()
    # Insert Into Table
    c.execute("INSERT INTO generates(store_id, invoice_id) VALUES (?,?)",[(box_store_id.get()),(box_invoice_id.get())])
    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close
    # Clear Text Boxes
    box_store_id.delete(0, END)
    box_invoice_id.delete(0, END)

def submit15():
    # Create a database or connect to one
    conn = sqlite3.connect('retail_database.sqlite')
    # Create cursor
    c = conn.cursor()
    # Insert Into Table
    c.execute("INSERT INTO in_stock(stk_id, product_id) VALUES (?,?)",[(box_stk_id.get()),(box_product_id.get())])
    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close
    # Clear Text Boxes
    box_stk_id.delete(0, END)
    box_product_id.delete(0, END)

def query():
    root = Tk()
    root.title('Showing the Records')
    root.geometry('{}x{}'.format(800, 400))

    # layout all of the main containers
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # create all of the main containers
    center = Frame(root, bg='light blue', padx=3, pady=3)
    center.grid(row=0, sticky="nsew")
     # Create a database or connect to one
    conn = sqlite3.connect('retail_database.sqlite')
    # Create cursor
    c = conn.cursor()
    # Query the database

    c.execute(box_query.get())
    records = c.fetchall()

    #Loop through results
    print_records = ""
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(center, text= print_records)
    query_label.grid(row=26, column=2, columnspan=2)

center = Frame(root, bg='light blue', padx=3, pady=3)
center.grid(row=0, sticky="nsew")

#Customer
box_cust_id = Entry(center, width = 15)
box_cust_id.grid(row = 0, column = 1, padx = 15)
box_c_name = Entry(center, width = 15)
box_c_name.grid(row = 1, column = 1, padx = 15)
box_c_phone = Entry(center, width = 15)
box_c_phone.grid(row = 2, column = 1, padx = 15)
box_c_address = Entry(center, width = 15)
box_c_address.grid(row = 3, column = 1, padx = 15)
box_c_email = Entry(center, width = 15)
box_c_email.grid(row = 4, column = 1, padx = 15)

cust_id = Label(center, text= "Customer ID: ")
cust_id.grid(row = 0, column = 0, padx = 15)
c_name = Label(center, text = "Customer Name: ")
c_name.grid(row = 1, column = 0, padx = 15)
c_phone = Label(center, text= "Customer Phone: ")
c_phone.grid(row = 2, column = 0, padx = 15)
c_address = Label(center, text=  "Customer Address: ")
c_address.grid(row = 3, column = 0, padx = 15)
c_email = Label(center, text=  "Customer Email: ")
c_email.grid(row = 4, column = 0, padx = 15)

#Purchases
box_product_id = Entry(center, width = 15)
box_product_id.grid(row = 14, column = 3, padx = 15)
box_username = Entry(center, width = 15)
box_username.grid(row = 15, column = 3, padx = 15)
box_password = Entry(center, width = 15)
box_password.grid(row = 16, column = 3, padx = 15)
box_cust_id = Entry(center, width = 15)
box_cust_id.grid(row = 17, column = 3, padx = 15)

product_id = Label(center, text= "Product ID: ")
product_id.grid(row = 14, column = 2, padx = 15)
username = Label(center, text= "Username: ")
username.grid(row = 15, column = 2, padx = 15)
password = Label(center, text = "Password: ")
password.grid(row = 16, column = 2, padx = 15)
cust_id = Label(center, text = "Customer ID: ")
cust_id.grid(row = 17, column = 2, padx = 15)


#Employee
box_e_id = Entry(center, width = 15)
box_e_id.grid(row = 0, column = 3, padx = 15)
box_e_ssn = Entry(center, width = 15)
box_e_ssn.grid(row = 1, column = 3, padx = 15)
box_e_name = Entry(center, width = 15)
box_e_name.grid(row = 2, column = 3, padx = 15)
box_e_title = Entry(center, width = 15)
box_e_title.grid(row = 3, column = 3, padx = 15)
box_e_start_date = Entry(center, width = 15)
box_e_start_date.grid(row = 4, column = 3, padx = 15)
box_e_end_date = Entry(center, width = 15)
box_e_end_date.grid(row = 5, column = 3, padx = 15)

e_id = Label(center, text= "Employee ID: ")
e_id.grid(row = 0, column = 2, padx = 15)
e_ssn = Label(center, text= "Employee SSN: ")
e_ssn.grid(row = 1, column = 2, padx = 15)
e_name = Label(center, text = "Employee Name: ")
e_name.grid(row = 2, column = 2, padx = 15)
e_title = Label(center, text= "Employee Title: ")
e_title.grid(row = 3, column = 2, padx = 15)
e_start_date = Label(center, text=  "Employee Start Date: ")
e_start_date.grid(row = 4, column = 2, padx = 15)
e_end_date = Label(center, text=  "Employee End Date: ")
e_end_date.grid(row = 5, column = 2, padx = 15)

#Invoice
box_invoice_id = Entry(center, width = 15)
box_invoice_id.grid(row = 0, column = 5, padx = 15)
box_cust_id = Entry(center, width = 15)
box_cust_id.grid(row = 1, column = 5, padx = 15)
box_store_id = Entry(center, width = 15)
box_store_id.grid(row = 2, column = 5, padx = 15)
box_total_amount = Entry(center, width = 15)
box_total_amount.grid(row = 3, column = 5, padx = 15)


invoice_id= Label(center, text= "Invoice ID: ")
invoice_id.grid(row = 0, column = 4, padx = 15)
cust_id = Label(center, text= "Customer ID: ")
cust_id.grid(row = 1, column = 4, padx = 15)
store_id = Label(center, text = "Store ID: ")
store_id.grid(row = 2, column = 4, padx = 15)
total_amount = Label(center, text= "Total Amount: ")
total_amount.grid(row = 3, column = 4, padx = 15)

#Stock
box_stk_id = Entry(center, width = 15)
box_stk_id.grid(row = 0, column = 7, padx = 15)
box_stk_address = Entry(center, width = 15)
box_stk_address.grid(row = 1, column = 7, padx = 15)
box_stk_item = Entry(center, width = 15)
box_stk_item.grid(row = 2, column = 7, padx = 15)
box_stk_type = Entry(center, width = 15)
box_stk_type.grid(row = 3, column = 7, padx = 15)

stk_id = Label(center, text= "Stock ID: ")
stk_id.grid(row = 0, column = 6, padx = 15)
stk_address = Label(center, text= "Stock Address: ")
stk_address.grid(row = 1, column = 6, padx = 15)
stk_item = Label(center, text = "Stock Item: ")
stk_item.grid(row = 2, column = 6, padx = 15)
stk_type = Label(center, text = "Stock Type: ")
stk_type.grid(row = 3, column = 6, padx = 15)

#Product
box_product_id = Entry(center, width = 15)
box_product_id.grid(row = 10, column = 3, padx = 15)
box_price= Entry(center, width = 15)
box_price.grid(row = 11, column = 3, padx = 15)
box_total_stock = Entry(center, width = 15)
box_total_stock.grid(row = 12, column = 3, padx = 15)

product_id = Label(center, text= "Product ID: ")
product_id.grid(row = 10, column = 2, padx = 15)
price = Label(center, text= "Price: ")
price.grid(row = 11, column = 2, padx = 15)
total_stock = Label(center, text = "Total Stock: ")
total_stock.grid(row = 12, column = 2, padx = 15)

#Supplier
box_supplier_id = Entry(center, width = 15)
box_supplier_id.grid(row = 10, column = 1, padx = 15)
box_supplier_name= Entry(center, width = 15)
box_supplier_name.grid(row = 11, column = 1, padx = 15)
box_supplier_address = Entry(center, width = 15)
box_supplier_address.grid(row = 12, column = 1, padx = 15)

supplier_id = Label(center, text= "Supplier ID: ")
supplier_id.grid(row = 10, column = 0, padx = 15)
supplier_name = Label(center, text= "Supplier Name: ")
supplier_name.grid(row = 11, column = 0, padx = 15)
supplier_address = Label(center, text = "Supplier Address: ")
supplier_address.grid(row = 12, column = 0, padx = 15)

#Store
box_store_id = Entry(center, width = 15)
box_store_id.grid(row = 10, column = 5, padx = 15)
box_s_phone = Entry(center, width = 15)
box_s_phone.grid(row = 11, column = 5, padx = 15)
box_s_address = Entry(center, width = 15)
box_s_address.grid(row = 12, column = 5, padx = 15)

store_id = Label(center, text= "Store ID: ")
store_id.grid(row = 10, column = 4, padx = 15)
s_phone = Label(center, text= "Store Phone: ")
s_phone.grid(row = 11, column = 4, padx = 15)
s_address = Label(center, text = "Store Address: ")
s_address.grid(row = 12, column = 4, padx = 15)

#Online Customer
box_cust_id = Entry(center, width = 15)
box_cust_id.grid(row = 10, column = 7, padx = 15)
box_username = Entry(center, width = 15)
box_username.grid(row = 11, column = 7, padx = 15)
box_password = Entry(center, width = 15)
box_password.grid(row = 12, column = 7, padx = 15)

cust_id = Label(center, text= "Customer ID: ")
cust_id.grid(row = 10, column = 6, padx = 15)
username = Label(center, text= "Username: ")
username.grid(row = 11, column = 6, padx = 15)
password = Label(center, text = "Password: ")
password.grid(row = 12, column = 6, padx = 15)

#Works
box_store_id = Entry(center, width = 15)
box_store_id.grid(row = 14, column = 5, padx = 15)
box_e_id = Entry(center, width = 15)
box_e_id.grid(row = 15, column = 5, padx = 15)
box_manager_id= Entry(center, width = 15)
box_manager_id.grid(row = 16, column = 5, padx = 15)

store_id = Label(center, text= "Store ID: ")
store_id.grid(row = 14, column = 4, padx = 15)
e_id = Label(center, text= "Employee ID: ")
e_id.grid(row = 15, column = 4, padx = 15)
manager_id = Label(center, text = "Manager ID: ")
manager_id.grid(row = 16, column = 4, padx = 15)

#Supplies
box_supplier_id = Entry(center, width = 15)
box_supplier_id.grid(row = 14, column = 1, padx = 15)
box_product_id = Entry(center, width = 15)
box_product_id.grid(row = 15, column = 1, padx = 15)

supplier_id = Label(center, text= "Supplier ID: ")
supplier_id.grid(row = 14, column = 0, padx = 15)
product_id = Label(center, text= "Product ID: ")
product_id.grid(row = 15, column = 0, padx = 15)

#Contains
box_store_id = Entry(center, width = 15)
box_store_id.grid(row = 19, column = 1, padx = 15)
box_product_id = Entry(center, width = 15)
box_product_id.grid(row = 20, column = 1, padx = 15)

store_id = Label(center, text= "Store ID: ")
store_id.grid(row = 19, column = 0, padx = 15)
product_id = Label(center, text= "Product ID: ")
product_id.grid(row = 20, column = 0, padx = 15)

#Customer Invoice
box_cust_id = Entry(center, width = 15)
box_cust_id.grid(row = 19, column = 3, padx = 15)
box_invoice_id = Entry(center, width = 15)
box_invoice_id.grid(row = 20, column = 3, padx = 15)

cust_id = Label(center, text= "Customer ID: ")
cust_id.grid(row = 19, column = 2, padx = 15)
invoice_id = Label(center, text= "Invoice ID: ")
invoice_id.grid(row = 20, column = 2, padx = 15)

#Generates
box_store_id = Entry(center, width = 15)
box_store_id.grid(row = 19, column = 5, padx = 15)
box_invoice_id = Entry(center, width = 15)
box_invoice_id.grid(row = 20, column = 5, padx = 15)

store_id = Label(center, text= "Store ID: ")
store_id.grid(row = 19, column = 4, padx = 15)
invoice_id = Label(center, text= "Invoice ID: ")
invoice_id.grid(row = 20, column = 4, padx = 15)

#In Stock
box_stk_id = Entry(center, width = 15)
box_stk_id.grid(row = 19, column = 7, padx = 15)
box_product_id = Entry(center, width = 15)
box_product_id.grid(row = 20, column = 7, padx = 15)

stk_id = Label(center, text= "Stock ID: ")
stk_id.grid(row = 19, column = 6, padx = 15)
product_id = Label(center, text= "Product ID: ")
product_id.grid(row = 20, column = 6, padx = 15)

#Online Account
box_username= Entry(center, width = 15)
box_username.grid(row = 14, column = 7, padx = 15)
box_password = Entry(center, width = 15)
box_password.grid(row = 15, column = 7, padx = 15)

username = Label(center, text= "Username: ")
username.grid(row = 14, column = 6, padx = 15)
password = Label(center, text= "Password: ")
password.grid(row = 15, column = 6, padx = 15)

# Create a Submit Button to Add Record
submit_btn = Button(center, text = "Add Record to Customer", command = submit)
submit_btn.grid(row=6, column = 0, columnspan = 2, pady=10, padx=10, ipadx= 20)

submit_btn1 = Button(center, text = "Add Record to Employee", command = submit1)
submit_btn1.grid(row=6, column = 2, columnspan = 2, pady=10, padx=10, ipadx= 20)

submit_btn2 = Button(center, text = "Add Record to Invoice", command = submit2)
submit_btn2.grid(row=6, column = 4, columnspan = 2, pady=10, padx=10, ipadx= 20)

submit_btn3 = Button(center, text = "Add Record to Stock", command = submit3)
submit_btn3.grid(row=6, column = 6, columnspan = 2, pady=10, padx=10, ipadx= 20)

submit_btn4 = Button(center, text = "Add Record to Supplier", command = submit4)
submit_btn4.grid(row=13, column = 0, columnspan = 2, pady=10, padx=10, ipadx= 20)

submit_btn5 = Button(center, text = "Add Record to Product", command = submit5)
submit_btn5.grid(row=13, column = 2, columnspan = 2, pady=10, padx=10, ipadx= 20)

submit_btn6 = Button(center, text = "Add Record to Store", command = submit6)
submit_btn6.grid(row=13, column = 4, columnspan = 2, pady=10, padx=10, ipadx= 20)

submit_btn7 = Button(center, text = "Add Record to Online Customer", command = submit7)
submit_btn7.grid(row=13, column = 6, columnspan = 2, pady=10, padx=10, ipadx= 20)

submit_btn8 = Button(center, text = "Add Record to Supplies", command = submit8)
submit_btn8.grid(row=18, column = 0, columnspan = 2, pady=10, padx=10, ipadx= 20)

submit_btn9 = Button(center, text = "Add Record to Purchases", command = submit9)
submit_btn9.grid(row=18, column = 2, columnspan = 2, pady=10, padx=10, ipadx= 20)

submit_btn10 = Button(center, text = "Add Record to Works", command = submit10)
submit_btn10.grid(row=18, column = 4, columnspan = 2, pady=10, padx=10, ipadx= 20)

submit_btn11 = Button(center, text = "Add Record to Online Account", command = submit11)
submit_btn11.grid(row=18, column = 6, columnspan = 2, pady=10, padx=10, ipadx= 20)

submit_btn12 = Button(center, text = "Add Record to Contains", command = submit12)
submit_btn12.grid(row=23, column = 0, columnspan = 2, pady=10, padx=10, ipadx= 20)

submit_btn13 = Button(center, text = "Add Record to Customer Invoice", command = submit13)
submit_btn13.grid(row=23, column = 2, columnspan = 2, pady=10, padx=10, ipadx= 20)

submit_btn14 = Button(center, text = "Add Record to Generates", command = submit14)
submit_btn14.grid(row=23, column = 4, columnspan = 2, pady=10, padx=10, ipadx= 20)

submit_btn15 = Button(center, text = "Add Record to In Stock", command = submit15)
submit_btn15.grid(row=23, column = 6, columnspan = 2, pady=10, padx=10, ipadx= 20)


# Create a Query Button
box_query = Entry(center, width = 40)
box_query.grid(row = 25, column=3, columnspan=2, pady=10, padx=10, ipadx=120)

query_btn = Button(center, text = "Show Records", command = query)
query_btn.grid(row=24, column=3, columnspan=2, pady=10, padx=10, ipadx=120)




conn.close

root.mainloop()