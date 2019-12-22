import json
import sqlite3

conn = sqlite3.connect('retail_database.sqlite')
c = conn.cursor()


#Create tables
try:
    c.executescript("""

    create table supplier
	(supplier_id		varchar(8),
	 supplier_name		varchar(30),
	 supplier_address	varchar(60),
	 primary key (supplier_id)
	);

create table supplies
( supplier_id		varchar(8),
product_id		varchar(8),
primary key (supplier_id, product_id)
foreign key(supplier_id) references supplier on delete cascade,
foreign key(product_id) references product on delete cascade
);

create table product
	(product_id		varchar(8), 
	 price		numeric(5,2) check (price > 0), 
	 total_stock integer(5),
	 primary key (product_id)
	);

create table purchases
	(product_id		varchar(8), 
	 username		varchar(30), 
	 password			varchar(10),
     cust_id varchar(8),
	 primary key (product_id, username, password, cust_id),
     foreign key(product_id) references product on delete cascade,
     foreign key(username) references online_acc on delete cascade,
     foreign key(password) references online_acc on delete cascade,
     foreign key(cust_id) references customer on delete cascade
	);

create table online_acc
	(username		varchar(30), 
	 password			varchar(10), 
	 primary key (username)
	);

create table online_cust
	(cust_id integer(8),
    username		varchar(30), 
	password			varchar(10), 
	primary key (cust_id, username, password)
    foreign key(cust_id) references customer on delete cascade,
    foreign key(username) references online_acc on delete cascade,
    foreign key(password) references online_acc on delete cascade
	);

create table customer
	(cust_id integer(8),
  c_name varchar(30),
  c_phone varchar(20),
  c_address varchar(60),
  c_email varchar (40),
  primary key (cust_id)
	);

create table cust_invoice
(cust_id integer(8),
invoice_id			integer(8),
primary key(cust_id, invoice_id),
foreign key(cust_id) references customer on delete cascade,
foreign key(invoice_id) references invoice on delete cascade
);

create table invoice
	(invoice_id			integer(8), 
    cust_id integer(8),
	 store_id			varchar(8),
     total_amount numeric(7,2) check (total_amount > 0),
     primary key (invoice_id),
     foreign key (cust_id) references customer (cust_id)
		on delete cascade,
     foreign key (store_id) references store (store_id)
		on delete cascade
	);

create table generates
	(store_id			integer(8),
    invoice_id			integer(8), 
    primary key(store_id, invoice_id)
    foreign key (store_id) references store (store_id)
		on delete cascade,
    foreign key(invoice_id) references invoice on delete cascade
);

create table contains
(store_id			integer(8), 
product_id		varchar(8),
primary key(store_id, product_id),
foreign key(store_id) references store on delete cascade,
foreign key(product_id) references product on delete cascade
);


create table store
	(store_id			integer(8), 
	 s_phone		varchar(20),
	 s_address	varchar(60),
	 primary key (store_id)
	);

create table works
	(store_id			integer(8),
    e_id			varchar(8), 
    manager_id			varchar(8), 
    primary key(store_id, e_id, manager_id)
    foreign key (store_id) references store (store_id)
		on delete cascade,
    foreign key(e_id) references employee on delete cascade
);

create table employee
	( e_id			varchar(8), 
      e_ssn			varchar(15),
      e_name		varchar(40),
	 e_title	varchar(20), 
   e_start_date varchar(20),
   e_end_date varchar(20),
   primary key (e_id)
	);

create table in_stock
	(stk_id		varchar(8),
    product_id		varchar(8),
	 primary key (stk_id, product_id),
    foreign key(product_id) references product on delete cascade,
     foreign key(stk_id) references stock on delete cascade
     );

create table stock
	(stk_id		varchar(8), 
   stk_address			varchar(60),
	 stk_item		varchar(25),
   stk_type varchar(20), 
	 primary key (stk_id)
	);""")


except: 
    pass

fname = input('Enter file name: ')

str_data = open(fname).read()
json_data = json.loads(str_data)

if fname == "CustomerJson.json":
    for entry in json_data['objects']:
        cust_id = entry['cust_id']
        c_name = entry['c_name']
        c_phone = entry['c_phone']
        c_address = entry['c_address']
        c_email = entry['c_email']

        c.execute("""INSERT OR IGNORE INTO customer(cust_id, c_name, c_phone, c_address, c_email) 
        VALUES (?,?,?,?,?)""",[(cust_id),(c_name),(c_phone),(c_address),(c_email)])

        conn.commit()

if fname == "cust_invoice.json":
    for entry in json_data:
        cust_id = entry['cust_id']
        invoice_id = entry['invoice_id']
    

        c.execute("""INSERT OR IGNORE INTO cust_invoice(cust_id, invoice_id) 
        VALUES (?,?)""",[(cust_id),(invoice_id)])

        conn.commit()

if fname == "in_stock.json":
    for entry in json_data:
        stk_id = entry['stk_id']
        product_id = entry['product_id']
    

        c.execute("""INSERT OR IGNORE INTO in_stock(stk_id, product_id) 
        VALUES (?,?)""",[(stk_id),(product_id)])

        conn.commit()

if fname == "generates.json":
    for entry in json_data:
        store_id = entry['store_id']
        invoice_id = entry['invoice_id']
    

        c.execute("""INSERT OR IGNORE INTO generates(store_id, invoice_id) 
        VALUES (?,?)""",[(store_id),(invoice_id)])

        conn.commit()

if fname == "contains.json":
    for entry in json_data:
        store_id = entry['store_id']
        product_id = entry['product_id']
    

        c.execute("""INSERT OR IGNORE INTO contains(store_id, product_id) 
        VALUES (?,?)""",[(store_id),(product_id)])

        conn.commit()

if fname == "works.json":
    for entry in json_data:
        store_id = entry['store_id']
        e_id = entry['e_id']
        manager_id = entry['manager_id']
    

        c.execute("""INSERT OR IGNORE INTO works(store_id, e_id, manager_id) 
        VALUES (?,?,?)""",[(store_id),(e_id), (manager_id)])

        conn.commit()

if fname == "online_cust.json":
    for entry in json_data:
        cust_id = entry['cust_id']        
        username = entry['username']
        password = entry['password']
    

        c.execute("""INSERT OR IGNORE INTO online_cust(cust_id, username, password) 
        VALUES (?,?,?)""",[(cust_id),(username),(password)])

        conn.commit()

if fname == "purchases.json":
    for entry in json_data:
        product_id = entry['product_id'] 
        username = entry['username']
        password = entry['password']
        cust_id = entry['cust_id'] 

        c.execute("""INSERT OR IGNORE INTO purchases(product_id, username, password, cust_id) 
        VALUES (?,?,?,?)""",[product_id,(username),(password),(cust_id)])

        conn.commit()


if fname == "SupplierJson.json":
    for entry in json_data['objects']:
        supplier_id = entry['supplier_id']
        supplier_name = entry['supplier_name']
        supplier_address = entry['supplier_address']


        c.execute("""INSERT OR IGNORE INTO supplier(supplier_id, supplier_name, supplier_address) 
        VALUES (?,?,?)""",[(supplier_id),(supplier_name),(supplier_address)])


        conn.commit()

if fname == "supplies.json":
    for entry in json_data:
        supplier_id = entry['supplier_id']
        product_id = entry['product_id']
    

        c.execute("""INSERT OR IGNORE INTO supplies(supplier_id, product_id) 
        VALUES (?,?)""",[(supplier_id),(product_id)])


        conn.commit()

if fname == "ProductJson.json":
    for entry in json_data['objects']:
        product_id = entry['product_id']
        price = entry['price']
        total_stock = entry['total_stock']


        c.execute("""INSERT OR IGNORE INTO product(product_id, price, total_stock) 
        VALUES (?,?,?)""",[(product_id),(price),(total_stock)])

        conn.commit()

if fname == "StoreJson.json":
    for entry in json_data['objects']:
        store_id = entry['store_id']
        s_phone = entry['s_phone']
        s_address = entry['s_address']


        c.execute("""INSERT OR IGNORE INTO store(store_id, s_phone, s_address) 
        VALUES (?,?,?)""",[(store_id),(s_phone),(s_address)])

        conn.commit()

if fname == "EmployeeJson.json":
    for entry in json_data['objects']:
        e_id = entry['e_id']
        e_ssn = entry['e_ssn']
        e_name = entry['e_name']
        e_title = entry['e_title']
        e_start_date = entry['e_start_date']
        e_end_date = entry['e_end_date']

        c.execute("""INSERT OR IGNORE INTO employee(e_id, e_ssn, e_name, e_title, e_start_date, e_end_date) 
        VALUES (?,?,?,?,?,?)""",[(e_id),(e_ssn),(e_name),(e_title),(e_start_date),(e_end_date)])

        conn.commit()

if fname == "StockJson.json":
    for entry in json_data['objects']:
        stk_id = entry['stk_id']
        stk_address = entry['stk_address']
        stk_item = entry['stk_item']
        stk_type = entry['stk_type']

        c.execute("""INSERT OR IGNORE INTO stock(stk_id, stk_address, stk_item, stk_type) 
        VALUES (?,?,?,?)""",[(stk_id),(stk_address),(stk_item), (stk_type)])

        conn.commit()

if fname == "invoice.json":
    for entry in json_data:
        store_id = entry['store_id']
        invoice_id = entry['invoice_id']
        cust_id = entry['cust_id']
        total_amount = entry['total_amount']

        c.execute("""INSERT OR IGNORE INTO invoice(invoice_id, cust_id, store_id, total_amount) 
        VALUES (?,?,?,?)""",[(invoice_id),(cust_id), (store_id), (total_amount)])

        conn.commit()

if fname == "OnlineAccJson.json":
    for entry in json_data['objects']:
        username = entry['username']
        password = entry['password']

        c.execute("""INSERT OR IGNORE INTO online_acc(username, password) 
        VALUES (?,?)""",[(username),(password)])

        conn.commit()

c.close()






