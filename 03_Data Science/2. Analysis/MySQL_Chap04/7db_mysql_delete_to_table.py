import csv
import MySQLdb
import sys

con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='open_source', passwd='1111')
c = con.cursor()

c.execute("""
        delete
        from Suppliers
        where Supplier_Name='Supplier Z'
        """)
con.commit()

c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)