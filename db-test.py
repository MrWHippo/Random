import sqlite3

conn = sqlite3.connect("test.db")
c = conn.cursor()

def create():
    c.execute('''
            CREATE TABLE IF NOT EXISTS products
            ([product_id] INTEGER PRIMARY KEY,
            [product_name] TEXT,
            [price] TEXT)
            ''')
    conn.commit()
###
def insert():
    c.execute('''
            INSERT INTO products (product_id, product_name, price)

                    VALUES
                    (1,'Computer','800'),
                    (2,'Printer','150'),
                    (3,'Tablet','400'),
                    (4,'Desk','60'),
                    (5,'Chair','40')
            ''')
    conn.commit()
###
def read():
    c.execute('''
            SELECT * FROM products''')

create()
insert()
read()
